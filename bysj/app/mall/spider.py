from lxml import etree
import time
import requests
import random
from threading import Thread
from app.my_models import *
import random
from app.mall.loc import loc_list
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
gid = 200000
goods_list = []
# loc_list = []

def parse(url, i):
    url = url.format(i)
    # print(url)
    html = requests.get(url=url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}).content.decode(
        'utf8', 'ignore')
    # with open('a.html','w') as f:
    #     f.write(html)
    # print(html)
    p = etree.HTML(html)
    # r_list = p.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[3]/a/em/text()')
    r_list = p.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li')
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[3]/a/em
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[2]/div/div[3]/a/em
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[3]/div/div[3]/a/em
    # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img
    # print(r_list)
    global goods_list
    goods_list = []
    # print(r_list)
    for item in r_list:
        # print(item)
        dic = {}
        global gid
        gid += 1
        dic['gid'] = gid
        # https://img14.360buyimg.com/n7/jfs/t1/14840/32/7616/240263/5c6e97ccEc6bb3736/c0d843e8041eb630.jpg
        # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[3]/a/em
        name = item.xpath('./div/div[3]/a/em/text()')[0].strip()
        price = item.xpath('./div/div[2]/strong/i/text()')[0].strip()
        # print(name)
        # print(price)
        # /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img
        try:
            pic = 'https:' + item.xpath('./div/div[1]/a/img/@src')[0]
            if not pic:
                pic = 'https:' + item.xpath('./div/div[1]/a/img/@source-data-lazy-img')[0]
        except Exception as e:
            continue
        # print(pic)
        pic_h = requests.get(url=pic,
                             headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 '
                                                    'Firefox/70.0'}).content
        with open('../static/goods_pic/' + str(gid) + '.jpg', 'wb') as f:
            f.write(pic_h)
        # print(pic_h)
        dic['name'] = name
        dic['price'] = price
        try:
            good = Good(name)
            good_pic = Good_pic()
            db.session.add(good)
            db.session.add(good_pic)
            good.g_id = gid
            good.price = price
            good.inventory = random.randint(50,200)
            good.title = name
            good.weight = random.randint(1,15)
            good.loc = random.choice(loc_list)['name']
            good_pic.gid = gid
            good_pic.default_pic = str(gid) + '.jpg'
            db.session.commit()
        except Exception as e:
            pass
        print(dic)
        goods_list.append(dic)
    # print(goods_list)


# print(goods_list)
# print(r_list)
# print(len(r_list))
# <a href="javascript:;" class="curr">(.*?)</a>
# /html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img
url = 'https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86' \
      '%9C%E4%BA%A7%E5%93%81&stock=1&page={}'
j = 0
for i in range(1, 50):
    # page02 = page01 + 30
    # page02 = page01+30
    # th = Thread(target=parse)
    # url = url.format(i, page01)
    parse(url, i)
    # parse(url,i,page02)
    time.sleep(0.5)
    # print(i, page01, page02)
"""-----------------------------------------------------------"""
print(goods_list)
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&qrst=1&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=3&s=90&click=0
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&qrst=1&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=1&s=30&click=0
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&qrst=1&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=5&s=150&click=0
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&qrst=1&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=7&s=210&click=0