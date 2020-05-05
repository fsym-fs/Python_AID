# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
import scrapy
import os

class PptPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     print(dict(item))
    #     return item
    # 重写get_media_requests()方法
    def get_media_requests(self, item, info):
        """把一堆是下载链接交给调度器入队列"""
        # 把meta包装到请求对象中
        yield scrapy.Request(url=item['ppt_download'],meta={'item':item})
    # 重写file_path方法,保存到相应路径
    def file_path(self, request, response=None, info=None):
        # FILES_SOTRE: '/home/tarena/桌面/month04/day09/code/Ppt/ppt'
        # filename:...
        # scrapy.Request()中所有参数都可以作为请求对象request的属性
        item = request.meta['item']
        filename = '{}/{}{}'.format(item['parent_name'],item['ppt_name'],os.path.splitext(request.url)[1])
        return filename
