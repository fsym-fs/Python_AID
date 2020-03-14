"""
    1.匹配一个ip地址
    2.匹配书名  《红与黑》
    3.匹配日期  2020-11-30  2020-1-5   2020-05-03
    4.匹配身份证号
"""
import re

# 匹配一个ip地址
try:
    r = re.search \
        (r"(0\.|1\d{0,2}\.|2\d\.|2[0-5]{2}\.){3}(0|1\d{0,2}|2\d|2[0-5]{2})", "192.168.1.1") \
        .group()
    print(r)
except:
    print("error")
