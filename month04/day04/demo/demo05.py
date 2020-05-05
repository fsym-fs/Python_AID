import requests
import time
import random
from hashlib import md5


class YdSpider:
    def __init__(self):
        # url是F12抓包的地址
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = headers

    def get_ts_salt_sign(self, word):
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        s = md5()
        st = "fanyideskweb" + word + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        s.update(st.encode())
        sign = s.hexdigest()
        return ts, salt, sign

    def get_result(self, word):
        # 获取ts.salt,sign
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "c91d26d39b64800355094f87325f9ed8",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # 网站返回的是json数据时
        html = requests.post(url=self.url, data=data, headers=self.headers).json()
        result = html['translateResult'][0][0]['tgt']
        print(result)
        print(html)

    def run(self):
        word = input('输入要翻译的单词:')
        self.get_result(word)


headers = {
    # 检查频率最高 - 3个
    "Cookie": "OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; _ntes_nnid=96bc13a2f5ce64962adfd6a278467214,1551873108952; JSESSIONID=aaae9i7plXPlKaJH_gkYw; td_cookie=18446744072941336803; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1565689460872",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()
