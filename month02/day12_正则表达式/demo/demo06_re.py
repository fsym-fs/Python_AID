"""
    re模块:match对象
"""
import re

pattern = r"(ab)cd(?P<dog>ef)"
regex = re.compile(pattern)
obj = regex.search("abcdefghki")
print(obj.group())
# 返回匹配到的内容在字符串中的位置
print(obj.span())
# 返回捕获组组名与其对应内容的字典
print(obj.groupdict())
print(obj.group('dog'))
