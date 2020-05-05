"""
    利用requests.get(cookies = {})
"""

import requests


def login():
    url = 'https://www.douban.com/people/215928531/'
    headers = {
        # 'Cookie': 'll="118166"; bid=pABQJSCpcZE; _vwo_uuid_v2=DEED200D4BE514A5E153D7964E1F68568|0be1dcc104941ca455453de9b838db40; __utmc=30149280; dbcl2="215928531:3WiPxw+oXIs"; ck=hcZp; ap_v=0,6.0; __gads=ID=725df348c6d3ee2a:T=1587952738:S=ALNI_MZYW2HNouy1LTr98m_CkWr9fctckA; push_noty_num=0; push_doumail_num=0; douban-profile-remind=1; _pk_id.100001.8cb4=351484fb54c60a29.1587958987.1.1587958987.1587958987.; _pk_ses.100001.8cb4=*; __utma=30149280.244687849.1587958987.1587958987.1587958987.1; __utmz=30149280.1587958987.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmv=30149280.21592; __utmb=30149280.2.10.1587958987',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    cook_str = 'll="118166"; bid=pABQJSCpcZE; _vwo_uuid_v2=DEED200D4BE514A5E153D7964E1F68568|0be1dcc104941ca455453de9b838db40; __utmc=30149280; dbcl2="215928531:3WiPxw+oXIs"; ck=hcZp; ap_v=0,6.0; __gads=ID=725df348c6d3ee2a:T=1587952738:S=ALNI_MZYW2HNouy1LTr98m_CkWr9fctckA; push_noty_num=0; push_doumail_num=0; douban-profile-remind=1; _pk_id.100001.8cb4=351484fb54c60a29.1587958987.1.1587958987.1587958987.; _pk_ses.100001.8cb4=*; __utma=30149280.244687849.1587958987.1587958987.1587958987.1; __utmz=30149280.1587958987.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmv=30149280.21592; __utmb=30149280.2.10.1587958987'
    cookies = get_cookies(cook_str)
    html = requests.get(url=url, headers=headers,cookies = cookies).text
    print(html)

def get_cookies(cook_str):
    lis = cook_str.split('; ')
    # print(lis)
    dic = {}
    for i in lis:
        # print(i.split('='))
        dic[i.split('=')[0]] = i.split('=')[1]
        # print(dic)
        # lis.append(dic)
    return dic

login()
