# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class GuaziPipeline(object):
    def process_item(self, item, spider):
        # print('i')
        # print(item['name'], item['link'], item['price'])
        print(dict(item))
        return item


# 管道二
import pymysql
from .settings import *


class GuaziMysqlPipeline(object):
    def open_spider(self, spider):
        """在爬虫启动时执行,只执行一次,一般用于链接数据库"""
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into cartab values (%s,%s,%s)'
        li = [
            item['name'], item['price'], item['link']
        ]
        self.cur.execute(ins, li)
        self.db.commit()
        return item

    def close_spider(self, spider):
        """在爬虫项目结束是,只执行一次,一般用户数据库断开"""
        self.cur.close()
        self.db.close()
