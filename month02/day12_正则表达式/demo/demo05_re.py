"""
    re模块:regex
"""
import re

s = "2020年2月19日"
patten = r"\d+"
it = re.finditer(patten, s)
# 返回匹配的match对象,每个match对应一处匹配结果
for i in it:
    print(i.group())

# 匹配目标字符串开始位置
obj = re.match(patten, s)
print(obj.group())

# 匹配第一处内容
obj = re.search(patten, s)
print(obj.group())
