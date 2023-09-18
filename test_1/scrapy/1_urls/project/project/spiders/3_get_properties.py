import scrapy
import os
import json
from ..utils.utils import utils, COOKIE_STRING
import re



class IndexSpider(scrapy.Spider):

    name = "get_properties"
    init_url = 'https://www.homegate.ch'
    url = 'https://www.homegate.ch/buy/real-estate/zip-1149/matching-list?be=50000'
    page = 1

    def format_seller_name(self, data):
        return data.strip() if data else None
    
    def format_phone_number(self, data):
        if not data or 'tel:' not in data: return data
        return data.split('tel:')[-1].replace(" ","")
    
    def format_property_type(self, data):
        if not data: return data
        match = re.search(r'<dd>(.*?)</dd>', data)
        return match.group(1).strip() if match else data

    def format_rooms(self, data):
        return float(data.strip()) if data else data

    def format_built_year(self, data):
        return int(data.strip()) if data else data
    
    def format_property_address(self, data):
        return ' '.join(data) if data else data
   
    def format_property_price(self, price):
        if not price: return price
        if '.– ' not in price: return price
        return price.split('.')[0].strip()
    
    def format_property_features(self, features):
        if not features: return features
        formatted_features = [
            feature.replace('<div>', '')
                    .replace('</div>', '')
            for feature in features
        ]
        result = "• " + "\n• ".join(formatted_features)
        return result

    def format_description(self, data):
        return "\n ".join(data) if data else data

    def start_requests(self):
        yield scrapy.Request(
            url = f'{self.url}&ep=1',
            headers = self.settings.get('HEADERS'),
            callback=self.get_all_properties
        )
    
    def get_all_properties(self, response, **kwargs):

        list_items = response.xpath('//div[@role="listitem"]')

        if not list_items: return

        for list_item in list_items:
            item_href = list_item.xpath('./div/a/@href').get()
            url = self.init_url + item_href
            yield scrapy.Request(
                url = url,
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
                    'cookie': 'serverExperiments=RUB-3215.1.SRP; __cf_bm=20b.GPnohuqyEuQfiQuvoydaashEO5Xby6V.v41h5gs-1694706004-0-AdQNdXL8wE20uFJXEGjhCR1WU9f34But5VNk7SLzqa+3Q1DV6M7NsqTStvgLYrykBAdAhYUNszBK2y83NXheR/k=; homegate_language=EN; homegate_language=EN; homegate_language=EN; OptanonAlertBoxClosed=2023-09-14T15:40:07.029Z; eupubconsent-v2=CPyEymgPyEymgAcABBENDWCsAP_AAH_AAAQ4Jqtf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdF-8N3f_X_L8X52M5vF36tqoKuR4ku3bBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PkmlMbM2dYGH9_n9_z-ZKY7___f__z_v-v___9____7-3f3__5__--__e_V_-9zfn9_____9vP___9v-_9_3________3_r9_7_D_-f_87_XW-4goAEmGhcQBdkSMhNtGEUCAEYVhIVQKACiASFogMIXVwU7K4CfWAiAECKAB4IAQwAoyABAAAJAEhEAEgRwIBAIBAIAAQAKhAIAGNgAHgBaCAQACgOhYpxQBKBYQZEJEQpgQhSJBQT2VCCUH6grhCGWWBFBo_4qEBCsgYrAiEhYvQ4AkBLxJIHuqN8ABCAFAKKUKxFJ-YAhwTNlqrxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAA.f_gAD_gAAAAA; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+14+2023+22%3A40%3A07+GMT%2B0700+(Indochina+Time)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=e87265f0-eab0-4979-aac8-0cf368731844&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CC0002%3A1%2CSTACK42%3A1; _uetsid=fb2c28f0531411ee88e897baf05cac98; _uetvid=fb2c4ff0531411ee93eadb690fd82e28; dakt_2_dnt=false; _gaexp=GAX1.2.pka_zdZwTDOuzPHpjsjqRA.19692.1; clientExperiments=pka_zdZwTDOuzPHpjsjqRA.Experiment.PDP_OR_SRP_OR_TENANTPLUS_PAYMENT; ln_or=eyIxMTI1MzMiOiJkIn0%3D; _gid=GA1.2.68435960.1694706008; _gat_UA-1084254-1=1; _ga=GA1.1.1816778141.1694706008; _ga_77SLSBFELK=GS1.1.1694706008.1.0.1694706008.0.0.0; _clck=2nvj0w|2|ff0|0|1352; FPID=FPID2.2.Rbas1trVxO5Ro8OYSGZ7Tadf8FkU8TKh64Dh7Jj7TrM%3D.1694706008; _clsk=k611ek|1694706009193|1|0|y.clarity.ms/collect; FPLC=OsZWkvnx6%2BDdDZA6mzevKcRXqiOqffnCTza67wNHV4OOjDbg6PS9mIl%2BndvYk%2FVtLBGS13o4uxHGysmMpQfFKwVKQIhR3kz9A%2BU1fmdhEARFzzYWFwf5z9xx5iuKCg%3D%3D'
                },
                callback=self.get_property_details,
                meta = {
                    'url': url
                }
            )
        
      
        self.page += 1
        if self.page == 50: return
        yield scrapy.Request(
            url = f'{self.url}&ep={self.page}',
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
                'cookie': 'serverExperiments=RUB-3215.1.SRP; __cf_bm=20b.GPnohuqyEuQfiQuvoydaashEO5Xby6V.v41h5gs-1694706004-0-AdQNdXL8wE20uFJXEGjhCR1WU9f34But5VNk7SLzqa+3Q1DV6M7NsqTStvgLYrykBAdAhYUNszBK2y83NXheR/k=; homegate_language=EN; homegate_language=EN; homegate_language=EN; OptanonAlertBoxClosed=2023-09-14T15:40:07.029Z; eupubconsent-v2=CPyEymgPyEymgAcABBENDWCsAP_AAH_AAAQ4Jqtf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdF-8N3f_X_L8X52M5vF36tqoKuR4ku3bBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PkmlMbM2dYGH9_n9_z-ZKY7___f__z_v-v___9____7-3f3__5__--__e_V_-9zfn9_____9vP___9v-_9_3________3_r9_7_D_-f_87_XW-4goAEmGhcQBdkSMhNtGEUCAEYVhIVQKACiASFogMIXVwU7K4CfWAiAECKAB4IAQwAoyABAAAJAEhEAEgRwIBAIBAIAAQAKhAIAGNgAHgBaCAQACgOhYpxQBKBYQZEJEQpgQhSJBQT2VCCUH6grhCGWWBFBo_4qEBCsgYrAiEhYvQ4AkBLxJIHuqN8ABCAFAKKUKxFJ-YAhwTNlqrxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAA.f_gAD_gAAAAA; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+14+2023+22%3A40%3A07+GMT%2B0700+(Indochina+Time)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=e87265f0-eab0-4979-aac8-0cf368731844&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CC0002%3A1%2CSTACK42%3A1; _uetsid=fb2c28f0531411ee88e897baf05cac98; _uetvid=fb2c4ff0531411ee93eadb690fd82e28; dakt_2_dnt=false; _gaexp=GAX1.2.pka_zdZwTDOuzPHpjsjqRA.19692.1; clientExperiments=pka_zdZwTDOuzPHpjsjqRA.Experiment.PDP_OR_SRP_OR_TENANTPLUS_PAYMENT; ln_or=eyIxMTI1MzMiOiJkIn0%3D; _gid=GA1.2.68435960.1694706008; _gat_UA-1084254-1=1; _ga=GA1.1.1816778141.1694706008; _ga_77SLSBFELK=GS1.1.1694706008.1.0.1694706008.0.0.0; _clck=2nvj0w|2|ff0|0|1352; FPID=FPID2.2.Rbas1trVxO5Ro8OYSGZ7Tadf8FkU8TKh64Dh7Jj7TrM%3D.1694706008; _clsk=k611ek|1694706009193|1|0|y.clarity.ms/collect; FPLC=OsZWkvnx6%2BDdDZA6mzevKcRXqiOqffnCTza67wNHV4OOjDbg6PS9mIl%2BndvYk%2FVtLBGS13o4uxHGysmMpQfFKwVKQIhR3kz9A%2BU1fmdhEARFzzYWFwf5z9xx5iuKCg%3D%3D'
            },
            callback=self.get_all_properties
        )

    def get_property_details(self, response):

        url = response.meta['url']

        # To do:
        # Phone Number
        # Other main information
        
        seller_name          = self.format_seller_name(response.xpath('//div[@class="ListingDetails_column_Nd5tM"]/p/text()').get())
        phone_number         = self.format_phone_number(response.xpath('//div[@class="ListingDetails_column_Nd5tM"][h2 = "Contact"]/div[@class="PhoneNumber_button_Tt5Yj"]/div[2]/a/@href').get())
        property_type        = self.format_property_type(response.xpath('//div[@class="CoreAttributes_coreAttributes_e2NAm"]/dl/dd[2]').get())
        rooms                = self.format_rooms(response.xpath('//dt[text()="No. of rooms:"]/following-sibling::dd[1]/text()').get())
        built_year           = self.format_built_year(response.xpath('//dt[text()="Year built:"]/following-sibling::dd/text()').get())
        property_address     = self.format_property_address(response.xpath('//address/span/text()').getall())
        price                = self.format_property_price(response.xpath('//div[@data-test="costs"]/dl/dd/strong/span/text()').get())
        property_features    = self.format_property_features(response.xpath('//ul[@class="FeaturesFurnishings_list_S54KV"]/li/div').getall())
        property_description = self.format_description(response.xpath('//div[@class="Description_descriptionBody_AYyuy"]/descendant-or-self::*/text()').getall())
        website              = response.xpath('//div[@class="ListingLink_linkItem_xSOJs"]/a/@href').get()

        yield {
            'url'                 : url,
            'seller_name'         : seller_name,
            'phone_number'        : phone_number,
            'email'               : None,
            'property_type'       : property_type,
            'rooms'               : rooms,
            'built_year'          : built_year,
            'property_address'    : property_address,
            'listing_status'      : None,
            'price'               : price,
            'property_features'   : property_features,
            'property_description': property_description,
            'local_amenties'      : None,
            'website'             : website,

            'available_from'      : available_from,
            'floors'              : floors, # https://www.homegate.ch/buy/3003145746
            'number_of_floors'    : number_of_floors,
            'number_of_apartments': number_of_apartments,
            'surface_living'      : surface_living,
            'floor_space'         : floor_space,
            'land_area'           : land_area, # https://www.homegate.ch/buy/3003533373
            'volume'              : volume, 
            'room_height'         : room_height,
            'last_refurbishment'  : last_refurbishment,

        }
