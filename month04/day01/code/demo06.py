# https://tieba.baidu.com/f?kw=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4&ie=utf-8&pn=0
# https://tieba.baidu.com/f?kw=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4&ie=utf-8&pn=100

# https://tieba.baidu.com/f?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&ie=utf-8&pn=0
"""
    百度贴吧数据抓取
"""

# 输入贴吧名
# 输入起始页
# 输入终止页
# 保存...吧...第...页.html

from urllib import parse
import requests
import time
import random


class TiebaSpider:
    def __init__(self):
        """
            定义常用变量
        """
        self.url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

    def get_html(self, url):
        """
            请求,获取html
        """
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self):
        """
            解析,数据解析提取
        """
        pass

    def save_html(self, filename, html):
        """
            数据处理功能
        """
        with open(filename, 'w', encoding='utf=8') as f:
            f.write(html)

    def run(self):
        """
            程序入口
        """
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        # 编码
        params = parse.quote(name)
        for page in range(start, end + 1):
            pn = (page - 1) * 50
            url = self.url.format(params, pn)
            html = self.get_html(url=url)
            filename = '{}_第{}页.html'.format(name, page)
            self.save_html(filename, html)
            # 控制爬取频率
            time.sleep(random.randint(1, 2))
            print('第{}页爬取完成'.format(page))


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()
