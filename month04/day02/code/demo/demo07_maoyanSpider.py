"""
猫眼电影top100抓取（电影名称、主演、上映时间）
"""
import requests
import re
import time
import random
import pymongo


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        self.on_mongo()
        self.li = []

    def on_mongo(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['maoyanset']

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # r_list: [('活着','牛犇','2000-01-01'),(),(),...,()]
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        for r in r_list:
            self.li.append({'name': r[0].strip(),'act': r[1].strip(),'time': r[2].strip()})

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.get_html(url=url)
            # 控制数据抓取频率:uniform()生成指定范围内的浮点数
            time.sleep(random.uniform(0, 1))
        self.myset.insert_many(self.li)


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
