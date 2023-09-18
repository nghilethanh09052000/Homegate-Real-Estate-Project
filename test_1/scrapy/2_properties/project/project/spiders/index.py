import scrapy
from scrapy.loader import ItemLoader
import os
from ..items import PropertyItem
from  ..utils.utils import utils
import pandas as pd
import random
import time
class IndexSpider(scrapy.Spider):

    name = "get_properties"
   

    def start_requests(self):

        houses_data_path = os.path.abspath('testing/house_urls.csv')    
        if not os.path.exists(houses_data_path):
            print(f"File {houses_data_path} does not exist")
            return        
        
        self.house_data = pd.read_csv(houses_data_path).to_dict(orient='records')
        self.length_house_data = len(self.house_data)
        self.index = int(self.index)

        yield scrapy.Request(
            url = self.house_data[self.index]['url'],
            headers = self.settings.get('HEADERS'),
            callback=self.get_property_details,
            meta = {
                'url': self.house_data[self.index]['url']
            }
        )

    def get_property_details(self, response):


        url = response.meta['url']
        
        loader = ItemLoader(item=PropertyItem(), response=response)
        loader.add_value('url', url)
        loader.add_xpath('seller_name', '//div[@class="ListingDetails_column_Nd5tM"]/p/text()')
        loader.add_xpath('phone_number', '//div[@class="ListingDetails_column_Nd5tM"][h2 = "Contact"]/div[@class="PhoneNumber_button_Tt5Yj"]/div[2]/a/@href')
        loader.add_xpath('property_type', '//div[@class="CoreAttributes_coreAttributes_e2NAm"]/dl/dd[2]')
        loader.add_xpath('rooms', '//dt[text()="No. of rooms:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('built_year', '//dt[text()="Year built:"]/following-sibling::dd/text()')
        loader.add_xpath('property_address', '//address/span/text()')
        loader.add_xpath('price', '//div[@data-test="costs"]/dl/dd/strong/span/text()')
        loader.add_xpath('property_features', '//ul[@class="FeaturesFurnishings_list_S54KV"]/li/div')
        loader.add_xpath('property_description', '//div[@class="Description_descriptionBody_AYyuy"]/descendant-or-self::*/text()')
        loader.add_xpath('website', '//div[@class="ListingLink_linkItem_xSOJs"]/a/@href')
        loader.add_xpath('available_from', '//dl/dt[text()="Available from:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('floors', '//dl/dt[text()="Floor:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('number_of_floors', '//dl/dt[text()="Number of floors:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('number_of_apartments', '//dl/dt[text()="Number of apartments:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('surface_living', '//dl/dt[text()="Surface living:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('floor_space', '//dl/dt[text()="Floor space:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('land_area', '//dl/dt[text()="Land area:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('volume', '//dl/dt[text()="Volume:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('room_height', '//dl/dt[text()="Room height:"]/following-sibling::dd[1]/text()')
        loader.add_xpath('last_refurbishment', '//dl/dt[text()="Last refurbishment:"]/following-sibling::dd[1]/text()')

        property_item = loader.load_item()
        data          = utils.submit_data(property_item)

        yield data

        self.index += 1
        if self.index < self.length_house_data:
            next_url = self.house_data[self.index]['url']
            delay = random.uniform(1, 10)
            print('Delay Time:--->', delay)
            time.sleep(delay)
        yield response.follow(
            url = next_url,
            headers = self.settings.get('HEADERS'),
            callback=self.get_property_details,
            meta = {
                'url': next_url
            }
        )


        