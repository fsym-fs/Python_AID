# http://www.dianping.com/topic/s_c_4430_33943_r5750
# http://www.dianping.com/topic/s_c_4430_33943_r5750/p2
# http://www.dianping.com/topic/s_c_4430_33943_r5750/p3
# /html/body/div[2]/div/div[2]/div[1]/div[1]/ul/li[1]/a/@href
"""
//*[@id="basic-info"]/h1/text()
"""
import requests
import random
from fake_useragent import UserAgent
from lxml import etree
url = 'http://www.dianping.com/topic/s_c_4430_33943_r5750/p1'
html = requests.get(url=url,headers={'User-Agent':UserAgent().random}).text
# print(html)
p = etree.HTML(html)
url = p.xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/ul/li[1]/a/@href')
for i in url:
    j = str(i).split('//')
    two_url = j[1]
