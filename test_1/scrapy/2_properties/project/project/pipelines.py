# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from scrapy.exceptions import DropItem
from .query_manager.spider_query_manager import SpiderQueryManager
from .query_manager.spider_queries import GetCategoriesQuery, GetUrlsQuery, GetPropertiesQuery

class PostgreSQLPipeline:

    def __init__(self, postgres_host, postgres_db, postgres_user, postgres_password, postgres_port):
        
        self.postgres_host = postgres_host
        self.postgres_db = postgres_db
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password
        self.postgres_port = postgres_port

        # Add Query Class For Each Spider:
        self.query_manager = SpiderQueryManager()
        self.query_manager.add_query_class('get_category_urls', GetCategoriesQuery)
        self.query_manager.add_query_class('get_urls', GetUrlsQuery)
        #self.query_manager.add_query_class('get_properties', GetPropertiesQuery)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            postgres_host=crawler.settings.get('POSTGRES_HOST'),
            postgres_db=crawler.settings.get('POSTGRES_DB'),
            postgres_user=crawler.settings.get('POSTGRES_USER'),
            postgres_password=crawler.settings.get('POSTGRES_PASSWORD'),
            postgres_port=crawler.settings.get('POSTGRES_PORT'),
        )

    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host=self.postgres_host,
            database=self.postgres_db,
            user=self.postgres_user,
            password=self.postgres_password,
            port=self.postgres_port,
        )
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        query_class = self.query_manager.get_query_class(spider_name=spider.name)
        if not query_class:
            self.logger.error("Could Not Find Spider Class And Queries")
            return
        insert_query, data = query_class.get_insert_query(item)

        try:
            # Execute the INSERT query with the data dictionary
            self.cursor.execute(insert_query, data)
            self.connection.commit()
        except Exception as e:
            # Log any error that occurs during the insertion and drop the item
            spider.logger.error(f"Error inserting data: {e}")
            self.connection.rollback()
            raise DropItem("Failed to insert item into PostgreSQL database")

        return item

    def create_table_if_not_exists(self):
        try:
            for query_class in self.query_manager.query_classes.values():
                create_table_query = getattr(query_class, "create_table_query")
                if create_table_query:
                    self.cursor.execute(create_table_query)
                    self.connection.commit()
        except Exception as e:
            self.logger.error(f"Error Creating Table {e}")
            self.close_spider()
                


