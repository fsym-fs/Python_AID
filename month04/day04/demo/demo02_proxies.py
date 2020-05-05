import requests
from lxml import etree
import re
import redis
from hashlib import md5
import pymysql
import sys

class GovementSpider(object):
    def __init__(self):
        self.index_url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        }
        # redis指纹增量
        self.r = redis.Redis(host='localhost',port=6379,db=0)

    def get_html(self,url):
        """请求功能函数"""
        html = requests.get(url=url,headers=self.headers).text

        return html

    def parse_html(self):
        one_html = self.get_html(url=self.url)
        one_xpath = ''
        href_list = self.xpath_func(html=one_html,xpath_bds=one_xpath)
        if href_list:
            two_url = 'http://www.mca.gov.cn' + href_list[0]
            self.parse_two_page(two_url)
        else:
            print('提取最新月份链接失败!')

    def xpath_func(self, html, xpath_bds):
        """解析功能函数"""
        p = etree.HTML(html)
        r_list = p.xpath(xpath_bds)

        return r_list

    def md5_url(self,url):
        """URL加密函数"""
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def get_false_url(self):
        """获取最新月份链接 - 假链接"""
        html = self.get_html(self.index_url)
        # 解析提取最新月份链接 - 假链接
        one_xpath = '//table/tr[2]/td[2]/a/@href'
        false_href_list = self.xpath_func(html,one_xpath)
        if false_href_list:
            false_href = false_href_list[0]
            false_url = 'http://www.mca.gov.cn' + false_href
            # 生成指纹
            finger = self.md5_url(false_url)
            # redis集合增量判断
            if self.r.sadd('govspider:fingers',finger):
                self.get_real_url(false_url)
            else:
                sys.exit('数据已是最新')
        else:
            print('提取最新月份链接失败')

    def get_real_url(self,false_url):
        """获取真链接"""
        # 嵌入JS执行URL跳转,提取真实链接
        html = self.get_html(false_url)
        regex = r'window.location.href="(.*?)"'
        pattern = re.compile(regex,re.S)
        true_url_list = pattern.findall(html)
        if true_url_list:
            true_url = true_url_list[0]
            # 提取具体的数据
            self.get_data(true_url)
        else:
            print('提取真实链接失败')

    def get_data(self,true_url):
        """提取具体的数据"""
        html = self.get_html(true_url)
        # xpath提取数据
        two_xpath = '//tr[@height="19"]'
        tr_list = self.xpath_func(html, two_xpath)
        for tr in tr_list:
            code_list = tr.xpath('./td[2]/text() | ./td[2]/span/text()')
            name_list = tr.xpath('./td[3]/text()')
            code = code_list[0].strip() if code_list else None
            name = name_list[0].strip() if name_list else None
            print(name, code)

    def run(self):
        """程序入口函数"""
        self.get_false_url()

if __name__ == '__main__':
  spider = GovementSpider()
  spider.run()