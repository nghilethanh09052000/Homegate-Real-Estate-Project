class SpiderQueryManager:
    def __init__(self):
        self.query_classes = {}

    def add_query_class(self, spider_name, query_class):
        self.query_classes[spider_name] = query_class

    def get_query_class(self, spider_name):
        return self.query_classes.get(spider_name)

    def remove_query_class(self, spider_name):
        if spider_name in self.query_classes:
            del self.query_classes[spider_name]
