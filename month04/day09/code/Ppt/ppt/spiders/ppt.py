# -*- coding: utf-8 -*-
import scrapy

from ..items import PptItem


class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/xiazai/']

    def parse(self, response):
        """一级页面解析函数,提取大分类的名称和链接"""
        # li_list:[<>,<>,<>....]
        li_list = response.xpath('//div[@class="col_nav clearfix"]/ul/li')
        for li in li_list[1:]:
            item = PptItem()
            item['parent_name'] = li.xpath('./a/text()').get()
            parent_url = 'http://www.1ppt.com' + li.xpath('./a/@href').get()
            # 把大分类的链接交给调度器
            yield scrapy.Request(url=parent_url, meta={'meta1': item, 'parent_url': parent_url},
                                 callback=self.get_total_page)

    def get_total_page(self, response):
        """提起所有大分类的总页数,并提交url给调度器"""
        meta1 = response.meta['meta1']
        parent_url = response.meta['parent_url']
        try:
            last_page_href = response.xpath('//ul[@class="pages"]//li[last()]/a/@href').get()
            # ppt_zongjie_20.html
            total_page = int(last_page_href.split('.')[0].split('_')[-1])
            # 拼接多页url地址
            for page in range(1, total_page + 1):
                # http://www.1ppt.com/xiazai/zongjie/ppt_zongjie_2.html
                print(parent_url)
                print(last_page_href)
                page_url = parent_url + '_'.join(last_page_href.split('.')[0].split('_')[:-1]) + '_' + str(
                    page) + '.html'
                a = last_page_href.replace(str(page), str(total_page))
                a = parent_url + a
                print('a', a)
                print('b', page_url)
                yield scrapy.Request(url=page_url, meta={'meta2': meta1}, callback=self.get_ppt_info)
        except Exception as e:
            # 此请求在第一级页面中已经交给调度器入队列,所以此处会直接对请求地址去重,不会再进入调度器
            # 调度器生成指纹的规则:url,method,请求体,进行sha1()加密生成指纹
            # 解决方案: dont_filter 参数
            yield scrapy.Request(url=parent_url, meta={meta1}, callback=self.get_ppt_info, dont_filter=True)

    def get_ppt_info(self, response):
        meta2 = response.meta['meta2']
        li_list = response.xpath('//ul[@class="tplist"]/li')
        for li in li_list:
            item = PptItem()
            item['ppt_name'] = li.xpath('./h2/a/text()').get()
            item['parent_name'] = meta2['parent_name']
            son_url = 'http://www.1ppt.com' + li.xpath('./a/@href').get()
            yield scrapy.Request(url=son_url, meta={'item': item}, callback=self.get_download_url)

    def get_download_url(self, response):
        """提取内容:PPT下载链接"""
        item = response.meta['item']
        item['ppt_download'] = response.xpath('//ul[@class="downurllist"]/li/a/@href').get()
        yield item
