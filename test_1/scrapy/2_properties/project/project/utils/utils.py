import random
from ..settings import USER_AGENT_LIST
from http.cookies import SimpleCookie
from datetime import datetime
import json

COOKIE_STRING = 'homegate_language=EN; homegate_language=EN; homegate_language=EN; OptanonAlertBoxClosed=2023-09-14T15:13:58.399Z; eupubconsent-v2=CPyEymgPyEymgAcABBENDWCsAP_AAH_AAAQ4Jqtf_X__b2_r-_7_f_t0eY1P9_7__-0zjhfdF-8N3f_X_L8X52M5vF36tqoKuR4ku3bBIUdlHPHcTVmw6okVryPsbk2cr7NKJ7PkmlMbM2dYGH9_n9_z-ZKY7___f__z_v-v___9____7-3f3__5__--__e_V_-9zfn9_____9vP___9v-_9_3________3_r9_7_D_-f_87_XW-4goAEmGhcQBdkSMhNtGEUCAEYVhIVQKACiASFogMIXVwU7K4CfWAiAECKAB4IAQwAoyABAAAJAEhEAEgRwIBAIBAIAAQAKhAIAGNgAHgBaCAQACgOhYpxQBKBYQZEJEQpgQhSJBQT2VCCUH6grhCGWWBFBo_4qEBCsgYrAiEhYvQ4AkBLxJIHuqN8ABCAFAKKUKxFJ-YAhwTNlqrxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAA.f_gAD_gAAAAA; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+14+2023+22%3A13%3A58+GMT%2B0700+(Indochina+Time)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=af066ad3-0612-43f7-9dd1-4c290a40349b&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CC0002%3A1%2CSTACK42%3A1; ln_or=eyIxMTI1MzMiOiJkIn0%3D; dakt_2_dnt=false; _gaexp=GAX1.2.pka_zdZwTDOuzPHpjsjqRA.19692.1; clientExperiments=pka_zdZwTDOuzPHpjsjqRA.Experiment.PDP_OR_SRP_OR_TENANTPLUS_PAYMENT; _uetsid=5447f400531111eeb11e690c32d488cb; _uetvid=54480f70531111eea3736fb10f976ff7; _gid=GA1.2.14135855.1694704439; _ga=GA1.1.446646786.1694704439; _ga_77SLSBFELK=GS1.1.1694704439.1.0.1694704439.0.0.0; _clck=bdre5b|2|ff0|0|1352; __gads=ID=42af2af508b0a599:T=1694704441:RT=1694704441:S=ALNI_Mbif2TRD2fGKpaUIQ_udl6IjIIdxg; __gpi=UID=00000c46edd1381d:T=1694704441:RT=1694704441:S=ALNI_MbjsKmDSmrgg45XsCrC8vAkSeo-EA; FPID=FPID2.2.uGu90DTw2kOAb8H8Bc4XJ3LaXmB%2BSQqdRSfrmVM1HaI%3D.1694704439; _clsk=1pid1pt|1694704440176|1|1|y.clarity.ms/collect; FPLC=bZDA3PXZ7alkE1LYriP4%2Fs1IXUX34IhDz%2BWBhR5iZMSQTV%2Bo%2FzSyLfLEybHIMU5PJ479SHrndkXVfWoTUVQrUtStU40%2B2R8H0G%2FU6sTyBxN8yqCWoMs4WUhBskxWag%3D%3D'

class UtilsProcess:
   
    #Random User Agent:
    def random_user_agent(self):
        return random.choice(USER_AGENT_LIST)   
    
    def cookie_parser(self, cookie_string = COOKIE_STRING):

        cookie = SimpleCookie()
        cookie.load(cookie_string)

        cookies = {}
        for key, morsel in cookie.items():
            cookies[key] = morsel.value
        return cookies

    def submit_data(self, item):
        return {
            'url'                 : item.get('url'),
            'seller_name'         : item.get('seller_name'),
            'phone_number'        : item.get('phone_number'),
            'email'               : item.get('email'),
            'property_type'       : item.get('property_type'),
            'rooms'               : item.get('rooms'),
            'built_year'          : item.get('built_year'),
            'property_address'    : item.get('property_address'),
            'listing_status'      : item.get('listing_status'),
            'price'               : item.get('price'),
            'property_features'   : item.get('property_features'),
            'property_description': item.get('property_description'),
            'local_amenties'      : item.get('local_amenties'),
            'website'             : item.get('website'),
            'available_from'      : item.get('available_from'),
            'floors'              : item.get('floors'), # https://www.homegate.ch/buy/3003145746
            'number_of_floors'    : item.get('number_of_floors'),
            'number_of_apartments': item.get('number_of_apartments'),
            'surface_living (m²)' : item.get('surface_living'),
            'floor_space (m²)'    : item.get('floor_space'),
            'land_area (m²)'      : item.get('land_area'), # https://www.homegate.ch/buy/3003533373
            'volume (m³)'         : item.get('volume'), 
            'room_height (m)'     : item.get('room_height'),
            'last_refurbishment'  : item.get('last_refurbishment'),
        }

utils = UtilsProcess()


