# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .settings import *


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item


class MaoyanMysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into maoyanab values (%s,%s,%s)'
        li = [
            item['name'], item['star'], item['time']
        ]
        self.cur.execute(ins, li)
        self.db.commit()
        print('112')
        return item

    def close_spider(self, spider):
        """在爬虫项目结束是,只执行一次,一般用户数据库断开"""
        self.cur.close()
        self.db.close()


# 管道3 - 存入MongoDB管道
# import pymongo
#
#
# class CarMongoPipeline(object):
#     def open_spider(self, spider):
#         self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
#         self.db = self.conn[MONGO_DB]
#         self.myset = self.db[MONGO_SET]
#
#     def process_item(self, item, spider):
#         car_dict = {
#             'name': item['name'],
#             'price': item['price'],
#             'url': item['url']
#         }
#         self.myset.insert_one(car_dict)
