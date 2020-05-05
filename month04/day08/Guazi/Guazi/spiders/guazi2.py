# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['www.guazi.com']

    # start_urls = ['https://www.guazi.com/dachang/buy/o1/#bread']

    # 删除start_urls
    # 重写start_requests()方法
    def start_requests(self):
        for o in range(1, 6):
            url = 'https://www.guazi.com/dachang/buy/o{}/#bread'.format(o)
            yield scrapy.Request(url=url, callback=self.parse_one_page)

    # o = 1
    # https://www.guazi.com/
    def parse_one_page(self, response):
        """解析提取数据：名称、链接、价格"""
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            # 给 items.py 中的类GuaziItem实例化
            item = GuaziItem()
            item['name'] = li.xpath('./a[1]/@title').get()
            item['link'] = 'https://www.guazi.com' + li.xpath('./a[1]/@href').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()

            # 将二级页面url交给调度器
            # meta,在不同的解析函数之间传递数据
            yield  scrapy.Request(url=item['link'],meta={'item':item},callback=self.parse_two_page)

            # 数据交给管道文件处理的方法 ：yield item
            # yield item

    def parse_two_page(self,response):
        """行驶里程,排量,变速箱"""
        item = response.meta['item']
        item['km'] = response.xpath('//ul[@class="assort clearfix"]/li[2]/span/text()').get()
        item['displace'] = response.xpath('//ul[@class="assort clearfix"]/li[3]/span/text()').get()
        item['typ'] = response.xpath('//ul[@class="assort clearfix"]/li[4]/span/text()').get()
        yield item

# 抓取数据交给管道  yield item
# URL地址交给调度器  yiekd scrapy.Eequest(url=...,callback=...)
