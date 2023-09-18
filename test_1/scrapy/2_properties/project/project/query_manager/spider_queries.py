class GetCategoriesQuery:

    create_table_query = """
        CREATE TABLE IF NOT EXISTS homegate_categories (
            id SERIAL PRIMARY KEY,
            category_url TEXT,
            code VARCHAR(4),
            lat FLOAT,
            long FLOAT,
            geo_type VARCHAR(255),
            ingestion_date DATE DEFAULT current_date
        )
    """
    
    @staticmethod
    def get_insert_query(item):
        data = {
            'category_url': item['category_url'],
            'code'        : item['code'],
            'lat'         : item['lat'],
            'long'        : item['long'],
            'geo_type'    : item['geo_type']
        }

        insert_query = """
            INSERT INTO homegate_categories
                (category_url, code, lat, long, geo_type)
            VALUES
                (%(category_url)s, %(code)s, %(lat)s, %(long)s, %(geo_type)s)
        """

        return insert_query, data



class GetUrlsQuery:
    create_table_query = """
        CREATE TABLE IF NOT EXISTS homegate_urls (
            id SERIAL PRIMARY KEY,
            url TEXT,
            code VARCHAR(255),
            category_url TEXT,
            ingestion_date DATE DEFAULT current_date
        )
    """
    
    @staticmethod
    def get_insert_query(item):
        data = {
            'url'         : item['url'],
            'code'        : item['code'],
            'category_url': item['category_url']
        }

        insert_query = """
            INSERT INTO homegate_urls
                (url, code, category_url)
            VALUES
                (%(url)s, %(code)s, %(category_url)s)
        """

        return insert_query, data

class GetPropertiesQuery:


    def get_insert_query(item):
        data = {
            'code': item['code'],
            'url': item['url']
        }

        insert_query = """
            INSERT INTO homegate_urls
                (code, url)
            VALUES
                (%(code)s, %(url)s)
        """

        return insert_query, data