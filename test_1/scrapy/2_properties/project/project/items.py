# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.loader.processors import MapCompose
from itemloaders.processors import MapCompose, TakeFirst, Join
import re
from w3lib.html import remove_tags


def format_space_string(data):
    return data.strip() if data else None

def format_float_type(data):
    return float(data.strip()) if data else data

def format_phone_number(data):
    if not data or 'tel:' not in data: return data
    return data.split('tel:')[-1].replace(" ","")

def format_property_type(data):
    if not data: return data
    try:
        remove_html_data = remove_tags(data)
    except:
        remove_html_data = None
    return remove_html_data

def format_year(data):
    return int(data.strip()) if data else data

def format_property_address(address): # => []
    return address if address else []

def format_property_price(price):
    if not price: return price
    if '.– ' not in price: return price
    return price.split('.')[0].strip()

def format_property_features(features): # => []
    return remove_tags(features)

def format_description(description): # => []
    return description if description else []


class PropertyItem(scrapy.Item):

    url = scrapy.Field(
        output_processor = TakeFirst()
    )

    seller_name = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )

    phone_number = scrapy.Field(
        input_processor = MapCompose(format_phone_number),
        output_processor = TakeFirst()
    )

    property_type = scrapy.Field(
        input_processor = MapCompose(format_property_type),
        output_processor = TakeFirst()
    )

    rooms = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )

    built_year = scrapy.Field(
        input_processor = MapCompose(format_year),
        output_processor = TakeFirst()
    )

    property_address = scrapy.Field(
        input_processor = MapCompose(format_property_address),
        output_processor = Join(' ')
    )

    price = scrapy.Field(
        input_processor = MapCompose(format_property_price),
        output_processor = TakeFirst()
    )

    property_features = scrapy.Field(
        input_processor = MapCompose(format_property_features),
        output_processor = Join("\n")
    )

    property_description = scrapy.Field(
        input_processor = MapCompose(format_description),
        output_processor = Join("\n")
    )

    website = scrapy.Field(
        output_processor = TakeFirst()
    )

    available_from = scrapy.Field(
        output_processor = TakeFirst()
    )

    floors = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
    
    number_of_floors = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
    
    number_of_apartments = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
    
    surface_living = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
   
    floor_space = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
   
    land_area = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
   
    volume = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
    
    room_height = scrapy.Field(
        input_processor = MapCompose(format_space_string),
        output_processor = TakeFirst()
    )
    
    last_refurbishment = scrapy.Field(
        input_processor = MapCompose(format_year),
        output_processor = TakeFirst()
    )