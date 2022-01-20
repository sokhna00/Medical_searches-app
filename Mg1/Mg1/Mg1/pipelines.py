import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Mg1Pipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient('localhost',27017)

        db = self.conn['1mg']
        self.collection = db['pv']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item