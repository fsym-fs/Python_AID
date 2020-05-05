"""
猫眼电影top100抓取（电影名称、主演、上映时间）
"""
import requests
import re
import time
import random
from fake_useragent import UserAgent
from lxml import etree
class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent': UserAgent().random}
    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        print(html)
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据"""
        p = etree.HTML(html)
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        print(dd_list)
        item = {}
        for dd in dd_list:
            item['name'] = dd.xpath('.//p[@class="name"]/a/@title')[0].strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(item)
        # r_list: [('活着','牛犇','2000-01-01'),(),(),...,()]

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.get_html(url=url)
            # 控制数据抓取频率:uniform()生成指定范围内的浮点数
            time.sleep(random.uniform(0,1))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()











