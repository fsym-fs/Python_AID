# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道1 - 终端打印输出
class GuaziPipeline(object):
    def process_item(self, item, spider):
        print(item['name'], item['price'], item['link'])
        return item

# 管道2 - 存入MySQL数据库
class GuaziMysqlPipeline(object):
    def process_item(self, item, spider):
        return item











