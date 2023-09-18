import scrapy
import pandas as pd
import os


class GetUrlsSpider(scrapy.Spider):

    name = "get_urls"
    init_url = 'https://www.homegate.ch'
    list_urls = []
    
    def start_requests(self):

        category_data_path = os.path.abspath('testing/category_urls.csv')
        houses_data_path   = os.path.abspath('testing/house_urls.csv')            
            
        # Check if the file exists
        if not os.path.exists(category_data_path):
            print(f"File {category_data_path} does not exist")
            return
        category_data = pd.read_csv(category_data_path)
        urls = category_data.to_dict(orient='records')

        if os.path.exists(houses_data_path): 
            houses_data = pd.read_csv(houses_data_path)
            houses_data_list = houses_data.to_dict(orient='records')
            self.list_urls = houses_data_list['url']

        for url in urls:
            for i in range(1, 51):
                category_url = f"{url.get('category_url')}?be=50000&ep={i}"
                yield scrapy.Request(
                    url = category_url,
                    headers = self.settings.get('HEADERS'),
                    callback = self.parse,
                    meta = {
                        'code': url['code'],
                        'category_url': category_url
                    }
                )
            

    def parse(self, response):

        code = response.meta['code']
        category_url = response.meta['category_url']

        list_items = response.xpath('//div[@role="listitem"]')

        if not list_items: return

        for list_item in list_items:

            item_href = list_item.xpath('./div/a/@href').get()
            url = self.init_url + item_href

            if url in self.list_urls: continue

            self.list_urls.append(url) # Check Duplicated
            
            yield {
                'url'         : url,
                'code'        : code,
                'category_url': category_url
            }