# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class KfcPipeline(object):
    def process_item(self, item, spider):
        # print(dict(item))
        return item


import pymysql
from .settings import *


class KfcMysqlPipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset='utf8')
        self.cursor = self.db.cursor()
        self.ins = 'insert into kfctab values(%s,%s,%s,%s,%s)'

    def process_item(self, item, spider):
        shop_li = [
            item['row_num'],
            item['store_name'],
            item['address_detail'],
            item['city_name'],
            item['province_name'],
        ]
        self.cursor.execute(self.ins, shop_li)
        self.db.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
