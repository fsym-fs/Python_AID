"""
    代理IP
"""
import requests
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0'}
proxies = {
    'http':'http://112.85.164.220:9999',
    'https':'https://112.85.164.220:9999'
}
html = requests.get(url=url, headers=headers, proxies=proxies).text
print(html)
