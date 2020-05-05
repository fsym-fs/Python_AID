import requests
import re
import time
import random


class CarSpider(object):
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    # 功能函数1 - 获取响应内容
    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text

        return html

    # 功能函数2 - 正则解析
    def re_func(self, regex, html):
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    # 爬虫函数开始
    def parse_html(self, one_url):
        one_html = self.get_html(one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        href_list = self.re_func(one_regex, one_html)
        for href in href_list:
            # 每便利一个汽车信息，必须要把此辆汽车所有数据提取完成后再提取下一辆汽车信息
            url = 'https://www.che168.com' + href

            # 获取一辆汽车的信息
            self.get_data(url)
            time.sleep(random.randint(1, 2))

    # 获取一辆汽车信息
    def get_data(self, url):
        two_html = self.get_html(url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b'
        item = {}
        car_info_list = self.re_func(two_regex, two_html)
        item['name'] = car_info_list[0][0].strip()
        item['km'] = car_info_list[0][1].strip()
        item['year'] = car_info_list[0][2].strip()
        item['type'] = car_info_list[0][3].split('/')[0].strip()
        item['displacement'] = car_info_list[0][3].split('/')[1].strip()
        item['city'] = car_info_list[0][4].strip()
        item['price'] = car_info_list[0][5].strip()
        print(item)

    def run(self):
        for p in range(1, 11):
            url = self.url.format(p)
            self.parse_html(url)


if __name__ == '__main__':
    spider = CarSpider()
    spider.run()
