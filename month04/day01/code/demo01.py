import requests

# get()方法得到的为响应对象
response = requests.get(url='http://www.jd.com/')
print(response)
# text属性 获取相应内容(字符串)
# content属性 获取响应内容(字节串)
# status_code HTTP响应码
# url 实际返回数据的url地址
