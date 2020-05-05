"""
    使用多线程抓取豆瓣电影
"""

import requests
from threading import Thread, Lock
import time
from fake_useragent import UserAgent
from queue import Queue


class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'
        # 创建
        self.q = Queue()
        self.lock = Lock()

    def url_in(self):
        """将所有url放入队列"""
        for start in range(0, 692, 20):
            page_url = self.url.format(start)
            self.q.put(page_url)

    def get_html(self,url):
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url,headers=headers).json()
        return html

    def parse_html(self):
        """线程事件函数,从队列中get()请求,解析"""
        while True:
            self.lock.acquire()
            if not self.q.empty():
                #
                # self.lock.acquire()
                url = self.q.get()
                self.lock.release()
                html = self.get_html(url=url)
                item = {}
                for one_film in html:
                    item['rank'] = one_film['rank']
                    item['name'] = one_film['title']
                    item['time'] = one_film['release_date']
                    item['score'] = one_film['score']
                    print(item)
            else:
                self.lock.release()
                break

    def run(self):
        self.url_in()
        t_list = []
        for i in range(3):
            t = Thread(target=self.parse_html())
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()

if __name__ == '__main__':
    star_time = time.time()
    spider = DoubanSpider()
    spider.run()
    end_time = time.time()
    print('time:%.2f',end_time-star_time)

