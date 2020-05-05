"""
    抓取租房
    https://km.lianjia.com/zufang/xishan23/pg2/#contentList
"""
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class LianjiaSpider:
    def __init__(self):
        self.url = 'https://km.lianjia.com/zufang/xishan23/pg{}/#contentList/'
        # 计数
        self.i = 0

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据函数"""
        p = etree.HTML(html)
        # 基准xpath
        li_list = p.xpath('//div[@class="content__list"]//div')
        """
        //div[@class="content__list"]//div
        //div[@class="content__list"]//div[1]//div//p[1]/a/text()
        //div[@class="content__list"]//div[1]//div//p[2]/a/text()
        //div[@class="content__list"]//div[1]//div//p[2]/text()
        //div[@class="content__list"]//div[1]//div//p[2]/a[1]/text()
        //div[@class="content__list"]//div[1]//div//p[2]/a[2]/text()
        //div[@class="content__list"]//div[1]//div//p[2]/a[3]/text()
        ['\n        ', '-', '-', '\n        ', '\n        40㎡\n        ', '东        ', '\n          1室1厅1卫        ', '\n      ']
        ['\n        ', '-', '-', '\n        ', '\n        13㎡\n        ', '南        ', '\n          4室1厅1卫        ', '\n      ']        
        for i in li_list[4:7]:
            print(i.strip())
        """


    def run(self):
        """程序入口函数"""
        for pg in range(1, 2):
            url = self.url.format(pg)
            self.get_html(url=url)
            # 控制爬取频率
            time.sleep(random.randint(1, 2))
        print('number:', self.i)


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
