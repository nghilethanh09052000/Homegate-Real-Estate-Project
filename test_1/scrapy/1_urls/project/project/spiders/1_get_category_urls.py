import scrapy
import os
from ..utils.utils import utils

class GetCategoriesSpider(scrapy.Spider):

    name = "get_category_urls"

    def start_requests(self):
        for i in range(10, 100):
            yield scrapy.Request(
                url = f'https://api.homegate.ch/geo/locations?lang=en&name={str(i)}&size=100',
                headers = {
                    'user-agent': utils.random_user_agent()
                },
                callback= self.parse
            )

    def parse(self, response):

        data = response.json()
        results = data['results']

        for result in results:

            geoLocation = result['geoLocation']

            code     = geoLocation['hg5']['en']
            lat      = geoLocation['center']['lat']
            long     = geoLocation['center']['lon']
            geo_type = geoLocation['type']

            if '-' in code: code = code.split('-')[-1]

            category_url = f'https://www.homegate.ch/buy/real-estate/zip-{code}/matching-list'

            yield {
                'category_url' : category_url,
                'code'         : code,
                'lat'          : lat,
                'long'         : long,
                'geo_type'     : geo_type
            }
