from lxml import etree
import time
import requests
from threading import Thread
# import entree
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=1&s=1&click=0
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=3&s=61&click=0
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=5&s=121&click=0

# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4
# %BA%A7%E5%93%81&stock=1&page={}&s={}&click=0
# 1 1
# 2 61
# 3 121
# 100001-
# https://search.jd.com/s_new.php?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=3&s=61&click=0
# url = 'https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86' \
#       '%9C%E4%BA%A7%E5%93%81&stock=1&page=1&s=31&click=0'
def parse(url,page):
    html = requests.get(url=url,headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 '
                                                   'Firefox/70.0'}).content.decode('utf8','ignore')
    p = etree.HTML(html)
    with open('a.html','w') as f:
        f.write(html)
    # r_list = p.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[3]/a/em/text()')
    r_list = p.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li')
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[3]/a/em
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[2]/div/div[3]/a/em
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[3]/div/div[3]/a/em
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img
    goods_list = []
    gid = 100000
    for item in r_list:
        dic = {}
        gid += 1
        dic['gid'] = gid
        # https://img14.360buyimg.com/n7/jfs/t1/14840/32/7616/240263/5c6e97ccEc6bb3736/c0d843e8041eb630.jpg
        name = item.xpath('./div/div[3]/a/em/text()')[0].strip()
        price = item.xpath('./div/div[2]/strong/i/text()')[0].strip()
        pic = item.xpath('./div/div[1]/a/img/@src')
        print(pic)
        dic['name'] = name
        dic['price'] = price
        goods_list.append(dic)
# print(goods_list)
# print(r_list)
# print(len(r_list))
# <a href="javascript:;" class="curr">(.*?)</a>
url = 'https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86' \
      '%9C%E4%BA%A7%E5%93%81&stock=1&page={}&s={}&click=0'
j = 0
for i in range(1,50,2):
    page01 = j*60+1
    page02 = page01 + 30
    # page02 = page01+30
    j += 1
    th = Thread(target=parse)
    url = url.format(i,page01)
    print(i,page01,page02)
