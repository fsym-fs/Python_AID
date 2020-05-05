# """
# <div class="movie-item-info">.*?<a href=".*?" title="(.*?)".*?</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)
# """
import re
import requests
from urllib import parse
import time
import random


#
# str = '<div class="movie-item-info">.*?<a href=".*?" title="(.*?)".*?</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
# patterns = re.compile(str, re.S)
# html = """
# <div class="movie-item-info">
#         <p class="name"><a href="/films/1375" title="活着" data-act="boarditem-click" data-val="{movieId:1375}">活着</a></p>
#         <p class="star">
#                 主演：葛优,巩俐,牛犇
#         </p>
# <p class="releasetime">上映时间：1994-05-17(法国)</p>    </div>
# """
# r_list = patterns.findall(html)
# print(r_list)
#
# """
# [('活着', '\n                主演：葛优,巩俐,牛犇\n        ', '上映时间：1994-05-17(法国)')]
# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0
# """
#

class TopMove():
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
        self.str = '<div class="movie-item-info">.*?<a href=".*?" title="(.*?)".*?</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        self.patterns = re.compile(self.str, re.S)

    def get_html(self, url):
        print(url)
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self, html):
        r_list = self.patterns.findall(html)
        new_list = []
        for r in r_list:
            name = r[0].strip()
            act = r[1].strip()
            time = r[2].strip()
            new_list.append((name,act,time))
        return new_list

    def save_html(self, filename, data):
        with open(filename, 'a', encoding='utf-8') as f:
            for i in data:
                f.write('name: %s   act: %s   time: %s\n' % (i[0], i[1], i[2]))

    def run(self):
        for i in range(1, 11):
            num = (i - 1) * 10
            url = self.url.format(num)
            html = self.get_html(url)
            data = self.parse_html(html)
            self.save_html('top_move.txt', data)
            print("第{}页保存完成".format(i))
            # 随机浮点数
            time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    move = TopMove()
    move.run()
