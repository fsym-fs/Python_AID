import requests
import random
import time
from lxml import etree
import csv

def login():
    # url = 'https://www.tianyancha.com/search/p{}?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500118'
    # url = 'https://www.tianyancha.com/search/p{}?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500101'
    # url = 'https://www.tianyancha.com/search/p{}?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500102'
    # url = 'https://www.tianyancha.com/search/p{}?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500103'
    url = 'https://www.tianyancha.com/search/p{}?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500104'
    headers = {
        'Cookie': 'TYCID=70c3a650869911eab9a92b449a4554f0; undefined=70c3a650869911eab9a92b449a4554f0; ssuid=2704801554; _ga=GA1.2.1770071786.1587780424; jsid=SEM-BAIDU-PZ2004-VI-000001; _gid=GA1.2.1692142453.1587969820; tyc-user-phone=%255B%252218883194481%2522%255D; aliyungf_tc=AQAAAGTiOFDo0AcAfTlfddHaZ7EcH1jX; csrfToken=o41ggEE9VNz61diDRVYnCdkQ; bannerFlag=false; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1587780420,1587969818,1587970144,1588042628; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg4MzE5NDQ4MSIsImlhdCI6MTU4Nzk3MDYwMCwiZXhwIjoxNjE5NTA2NjAwfQ.rTQzKcGCPt7aQM9s7BxfPMNQNN8XLbVkwUD-cI7XOIpAkS3GOeE8BQvyg3gC9MCLyF_NfFjFF5d1Qt-m_-e77g%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%2596%25AF%25E5%259D%25A6%25E5%2588%25A9%25C2%25B7%25E5%259B%25BE%25E5%25A5%2587%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218883194481%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg4MzE5NDQ4MSIsImlhdCI6MTU4Nzk3MDYwMCwiZXhwIjoxNjE5NTA2NjAwfQ.rTQzKcGCPt7aQM9s7BxfPMNQNN8XLbVkwUD-cI7XOIpAkS3GOeE8BQvyg3gC9MCLyF_NfFjFF5d1Qt-m_-e77g; RTYCID=beaf3d01cd2d4f2d8499f53476397202; CT_TYCID=882a1a51157f47189e8c08aaec103720; cloud_token=6b40dfa82d9548d4ac608ff093f3287a; cloud_utm=8b908dad405044098eb4725a740d8add; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1588042831',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    ll = []
    for i in range(1, 6):
        o_url = url.format(i)
        html = requests.get(url=o_url, headers=headers).text
        # print(html)
        p = etree.HTML(html)
        lis = p.xpath('//*[@id="web-content"]/div/div[1]/div[4]/div[2]/div')
        for li in lis:
            item = {}
            fz = li.xpath('./div/div[3]/div[1]/a/em/text()')
            # print(fz)
            item['com'] = (li.xpath('./div/div[3]/div[1]/a/text()'))
            # print(item['com'])
            if item['com']:
                try:
                    item['com'] = item['com'][0] + fz[0] + item['com'][1]
                except:
                    item['com'] = item['com'][0]
            item['user'] = li.xpath('./div/div[3]/div[3]/div[1]/a/text()')
            if not item['user']:
                item['user'] = li.xpath('./div/div[3]/div[2]/div[1]/a/text()')
            item['phone'] = li.xpath('./div/div[3]/div[4]/div/span[2]/span/text()')
            if not item['phone']:
                item['phone'] = li.xpath('./div/div[3]/div[3]/div/span[2]/span/text()')
            if item['phone']:
                item['phone'] = str(item['phone'][0])
            print(item)
            ll.append((item['com'],item['user'],item['phone']))
        time.sleep(random.randint(1,2))
    print(ll)
    with open('spider_大渡口.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(ll)
    # with open('h.html','w') as f:
    #     f.write(html)


login()

# https://www.tianyancha.com/search/p1?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500118
# https://www.tianyancha.com/search/p2?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500118
# https://www.tianyancha.com/search/p3?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500118
# https://www.tianyancha.com/search/p4?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500118
# https://www.tianyancha.com/search/p5?key=%E6%9C%8D%E8%A3%85&base=cq&areaCode=500118
# //*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[?]
# //*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a
# //*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a/@href
# //*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[3]/div[1]/a
# or
# //*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[4]/div/div[3]/div[2]/div[1]/a/text()
# //*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[4]/div/span[2]/span
# or
# //*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[4]/div/div[3]/div[3]/div/span[2]/span[1]
# ------------------------------------------------------------------------------
# //*[@id="_container_baseInfo"]/table[2]/tbody/tr[10]/td[2]
