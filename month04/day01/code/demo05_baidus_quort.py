'''
    输入搜索的关键字,把响应的内容保存到本地文件
'''
import requests
from urllib import parse

# 拼接url地址
url = 'http://www.baidu.com/s?wd={}'
key = input('请输入关键字:')
parmas = parse.quote(key)
url = url.format(parmas)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
# 发送请求,获取响应内容
html = requests.get(url=url, headers=headers).text
print(html)
# 保存到本地文件
filename = '{}.html'.format(key)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
