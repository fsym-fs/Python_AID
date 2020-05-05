# -*- coding: utf-8 -*-
import scrapy


class BaixiaoduSpider(scrapy.Spider):
    name = 'baixiaodu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        """ 解析提取所需数据 """
        # 可以直接调用xpath
        # [<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]
        # extract():['字符串']
        # extract_first():'...'
        # 同 extract_first()
        result = response.xpath('/html/head/title/text()').get()

        print(result)
        print('*'*50)
