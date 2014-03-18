'''
Created on Mar 14, 2014

@author: cla
'''
from pymongo.connection import MongoClient
import traceback
from scrapy import log
import json

class BbsCrawlerPipeline(object):
    
    def __init__(self, mongodb_server = "localhost",\
                 mongodb_port = 27017, mongodb_db = "bbs_crawler",\
                 mongodb_collection = "job"):
        self.mongodb_server = mongodb_server
        self.mongodb_port = mongodb_port
        self.mongodb_db = ""
        self.mongodb_collection = ""
        try:
            connection = MongoClient(self.mongodb_server, self.mongodb_port)
            self.mongodb_db = connection[mongodb_db]
            self.mongodb_collection = self.mongodb_db[mongodb_collection]
        except Exception as e:
            print "Error while connecting mongodb!"
            traceback.print_exc()
            
    @classmethod
    def from_crawler(cls, crawler):
        return cls("localhost", 27017, "bbs_crawler", "job")
        
    def process_item(self, item, spider):
        if spider.name == 'sjtu' or spider.name == 'newsmth':
            job = {
                   'title': item['title'],
                   'link': item['link'],
                   'content': item['content'],
                   'domain': item['domain'],
                   }
            print self.mongodb_collection.find({'title': job['title']}).count()
            if self.mongodb_collection.find({'title': job['title']}).count() == 0:
                print job['title']
                result = self.mongodb_collection.insert(job)
                log.msg("item %s written into %s" %(result, self.mongodb_db), level = log.DEBUG, spider = spider)
        elif spider.name == 'sjtupre':
            json_file = open('sjtupre.json', 'wb')
            json_file.write(json.dumps(dict(item)))
            json_file.close()
            print spider.name 
        return item