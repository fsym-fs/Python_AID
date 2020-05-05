# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义字段
    # 大分类名字,ppt模板名字,ppt下载链接
    parent_name = scrapy.Field()
    ppt_name = scrapy.Field()
    ppt_download = scrapy.Field()
