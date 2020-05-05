"""
    https://accounts.douban.com/j/mobile/login/basic
    requests.session()实现模拟登录
    1.实例化对象
    2.登录网站 ---s.post()
    3.抓取数据 ---s.get()
"""
import requests

s = requests.session()


def login():
    # 登录
    post_url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = {
        'ck': '',
        'name': '15851702713',
        'password': '223751093QWE',
        'remember': 'false',
        'ticket': '',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Cookie': 'll="118166"; bid=pABQJSCpcZE; _vwo_uuid_v2=DEED200D4BE514A5E153D7964E1F68568|0be1dcc104941ca455453de9b838db40; apiKey=; __utmc=30149280; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2215851702713%22%2C%22code%22:%224916%22}; vtoken=phone_register%201fb3bf97f79f48e18e6dd5a68d6ec51b; __gads=ID=725df348c6d3ee2a:T=1587952738:S=ALNI_MZYW2HNouy1LTr98m_CkWr9fctckA; push_noty_num=0; push_doumail_num=0; douban-profile-remind=1; __utmv=30149280.21592; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1587968305%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2F215928531%2F%22%5D; _pk_ses.100001.2fad=*; last_login_way=account; ap_v=0,6.0; __utma=30149280.244687849.1587958987.1587958987.1587968352.2; __utmz=30149280.1587968352.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt=1; __utmb=30149280.2.10.1587968352; _pk_id.100001.2fad=da5ee052942a7de5.1587968305.1.1587968392.1587968305.; login_start_time=1587968395829'
    }

    s.post(url=post_url, data=data, headers=headers)
    # 抓取数据
    get_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    }
    get_url = 'https://www.douban.com/people/215928531/'
    html = s.get(url=get_url, headers=get_headers).text
    print(html)


login()
