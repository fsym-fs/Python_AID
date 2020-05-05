"""
打开浏览器，输入京东地址(https://www.jd.com/)，得到响应内容
"""
import requests

res = requests.get('https://www.jd.com/')
html = res.text
print(html)