"""
    https://nj.lianjia.com/ershoufang/pg2/
"""
from fake_useragent import UserAgent
from lxml import etree

import pymongo
import requests
import re
import time
import random


class LianjiaSpider:
    def __init__(self):
        self.url = 'https://nj.lianjia.com/ershoufang/pg{}/'
        # 1.连接对象
        self.conn = pymongo.MongoClient("localhost", 27017)
        # 2.库对象
        self.db = self.conn["lianjia"]
        # 3.集合对象
        self.myset = self.db["lianjiaset"]
        self.i = 1

    def get_heads(self):
        headers = {"User-Agent": UserAgent().random}
        return headers

    def get_html(self, url):
        # for i in range(3):
        #     try:
        #         html = requests.get(url=url, headers=self.get_heads(), timeout=3).content.decode('utf-8', 'ignore')
        #         data_list = self.parse_html(html)
        #         return data_list
        #     except Exception as e:
        #         print('Retry')
        html = requests.get(url=url, headers=self.get_heads()).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据"""
        p = etree.HTML(html)
        # 基准xpath：每个房源信息的节点对象dd列表
        div_list = p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        data_list = []
        for div in div_list:
            item = {}
            item['it'] = self.i
            self.i += 1
            name_list = div.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item["name"] = name_list[0].strip() if name_list else None
            address_list = div.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item["address"] = address_list[0].strip() if address_list else None

            info_list = div.xpath('.//div[@class="houseInfo"]/text()')
            if info_list:
                house_list = info_list[0].split('|')
                if len(house_list) == 7:
                    item['model'] = house_list[0].strip()
                    item['area'] = house_list[1].strip()
                    item['direct'] = house_list[2].strip()
                    item['perfect'] = house_list[3].strip()
                    item['floor'] = house_list[4].strip()
                    item['year'] = house_list[5].strip()
                    item['type'] = house_list[6].strip()
                else:
                    item['model'] = item['area'] = item['direct'] = item['perfect'] = item['floor'] = item['year'] = \
                        item['type'] = None
            else:
                item['model'] = item['area'] = item['direct'] = item['perfect'] = item['floor'] = item['year'] = \
                    item['type'] = None

            total_list = div.xpath('.//div[@class="totalPrice"]/span/text()')
            item["total"] = total_list[0].strip() if total_list else None
            unit_list = div.xpath('.//div[@class="unitPrice"]/span/text()')
            item["unit"] = unit_list[0].strip() if unit_list else None
            # print(item)
            data_list.append(item)
        print(data_list)
        self.save_html(data_list)

    def save_html(self, data_list):
        """数据处理函数"""
        self.myset.insert_many(data_list)

    def run(self):
        """程序入口函数"""
        for pg in range(0, 10, 1):
            url = self.url.format(pg)
            data_list = self.get_html(url=url)
            # 控制数据抓取频率:uniform()生成指定范围内的浮点数
            time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
