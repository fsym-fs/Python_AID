# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import re

from ..items import KfcItem


class KfcSpider(scrapy.Spider):
    name = 'kfc'
    allowed_domains = ['www.kfc.com.cn']

    # start_urls = ['http://www.kfc.com.cn/']
    # v 重写start_requests()方法,把所有需要抓取的请求交给调度器入队列
    def start_requests(self):
        """生成所有post请求,交给调度器入队列"""
        # 所有城市的列表
        all_city = self.get_all_city()
        for city in all_city:
            # 每个城市门店总页数
            total = self.get_total(city)
            for page in range(1, total + 1):
                post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
                formdata = {
                    'cname': city,
                    'pid': '',
                    'pageIndex': str(page),
                    'pagesize': '10'
                }
                yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.detail_page)

    # //ul[@class="shen_info"]/li[?]/strong/text()
    # //ul[@class="shen_info"]/li[?]/div[@class="shen_city"]/a[?]/text()
    # <a href="javascript:void(0);" title="" cityid="3064" rel="安庆" class="">安庆</a>
    # <a href=".*?rel="(.*?)">
    def get_all_city(self):
        """获取所有城市列表"""
        url = 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
        html = requests.get(url=url, headers=headers).text
        regex = '<a href=".*?rel="(.*?)">'
        pattern = re.compile(regex, re.S)
        all_city = pattern.findall(html)
        return all_city

    def get_total(self, city):
        """获取每个城市门店总页数"""
        post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
        data = {
            'cname': city,
            'pid': '',
            'pageIndex': '1',
            'pagesize': '10'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
        html = requests.post(url=post_url, headers=headers, data=data).json()
        count = html['Table'][0]['rowcount']
        total = count // 10 if count % 10 == 0 else count // 10 + 1
        return total

    def detail_page(self, response):
        """解析提取具体门店数据"""
        html = json.loads(response.text)
        for kfc_shop in html['Table1']:
            item = KfcItem()
            item['row_num'] = kfc_shop['rownum']
            item['store_name'] = kfc_shop['storeName'].strip()
            item['address_detail'] = kfc_shop['addressDetail'].strip()
            item['city_name'] = kfc_shop['cityName'].strip()
            item['province_name'] = kfc_shop['provinceName'].strip()
            yield item

    def parse(self, response):
        pass
