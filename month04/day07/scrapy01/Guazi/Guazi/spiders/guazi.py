# -*- coding: utf-8 -*-
import scrapy


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/dachang/buy/']

    def parse(self, response):
        # //ul[@class = 'carlist clearfix js-top']/li
        li_list = response.xpath("//ul[@class = 'carlist clearfix js-top']/li")
        for li in li_list:
            item = {}
            item['name'] = li.xpath('./a[1]/@title').get()
            item['link'] = li.xpath('./a[1]/@href').get()
            print(item)
