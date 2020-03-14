"""
    re模块:regex
"""
import re

# 目标字符串
s = "Alex:1996,Sunny:1998"
# 正则表达式
pattern01 = r"(\w+):(\d+)"
pattern02 = r"\w+:\d+"
# re模块调用findall
l = re.findall(pattern01, s)
print(l)
# 正则表达式对象调用
regex = re.compile(pattern02)
# s[0:13]作为匹配对象
l = regex.findall(s, 0, 13)
print(l)

# 对目标字符串进行切割
l = re.split(r":|,", s, 2)
print(l)

# 替换匹配到的内容
s = re.sub(r":", "--", s, 1)
print(s)

