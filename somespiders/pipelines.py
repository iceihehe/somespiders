# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.Connection(
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTIONS']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
        return item
