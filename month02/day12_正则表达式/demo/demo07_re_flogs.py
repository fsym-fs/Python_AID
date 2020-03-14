"""
    re模块:flogs
"""
import re

s = """Hello
北京
"""
# 只匹配ascill码
regex = re.compile(r"\w+", flags=re.A)
l = regex.findall(s)
print(l)

# 让.可以匹配换行
regex = re.compile(r".+", flags=re.S)
l = regex.findall(s)
print(l)

# 忽略大小写
regex = re.compile(r"[a-z]+", re.I)
l = regex.findall(s)
print(l)

# 让^和$可以匹配每一行的起始位置
regex = re.compile(r"^北京", re.M)
l = regex.findall(s)
print(l)
