import re

# 匹配所有数字
from typing import List, Any

r = re.findall("\d+", "今天是2020年2月19日")
print(r)  # ['2020', '2', '19']

# 普通字符，匹配字符串中对应字符
r = re.findall("a", "abcderad")
print(r)  # ['a', 'a']

"""
    或关系:
        元字符:|
        匹配 | 两侧任意的正则表达式,不能重叠
        
"""
r = re.findall("ab|ef", "abcdefabcd")
print(r)  # ['ab', 'ef', 'ab']

"""
    匹配单个字符:
        元字符:.
        匹配规则：匹配除换行外的任意一个字符
"""
r = re.findall("A.", "A12,A14,A15")
print(r)  # ['A1', 'A1', 'A1']

"""
    匹配字符集
    元字符:[字符集]
    匹配规则: 匹配字符集中的任意一个字符
    表达形式:
    [abc#!好] 表示 [] 中的任意一个字符
    [0-9],[a-z],[A-Z] 表示区间内的任意一个字符
    [_#?0-9a-z] 混合书写，一般区间表达写在后面
"""
r = re.findall("[aeiou]", "How are you")
print(r)  # ['o', 'a', 'e', 'o', 'u']

"""
    匹配字符集反集
    元字符:[^字符集]
    匹配规则:匹配除了字符集以外的任意一个字符

"""
r = re.findall("[^abcr]", "How are you")
print(r)  # ['H', 'o', 'w', ' ', 'e', ' ', 'y', 'o', 'u']

"""
    匹配字符串开始位置
    元字符: ^
    匹配规则：匹配目标字符串的开头位置
"""
r = re.findall("^am", "Jame")
print(r)  # []
r = re.findall("^Ja", "Jame")
print(r)  # ['Ja']

"""
    匹配字符串结尾位置
    元字符: $
    匹配规则：匹配目标字符串的结尾位置
"""
r = re.findall("am$", "Jame")
print(r)  # []
r = re.findall("me$", "Jame")
print(r)  # ['me']

"""
    匹配字符重复
    元字符: *
        匹配规则：匹配前面的字符出现0次或多次
    元字符:+
        匹配规则： 匹配前面的字符出现1次或多次
    元字符:?
        匹配规则： 匹配前面的字符出现0次或1次
    元字符:{n}
    匹配规则： 匹配前面的字符出现n次
    元字符:{m,n}
    匹配规则： 匹配前面的字符出现m-n次
"""
r = re.findall("wo*", "wow,wooooow,wowowo")
print(r)
r = re.findall("wo+", "wow,wooooow,wowowo")
print(r)
r = re.findall("[0-9]+", "今天是2020年2月19日")
print(r)
r = re.findall("[A-Z][a-z]+", "Hi,Jame How are you")
print(r)
r = re.findall("-?[0-9]+", "12 -45 256 -1 6")
print(r)
r = re.findall("1[0-9]{10}", "13915172110")
print(r)
r = re.findall("[1-9][0-9]{4,10}", "1085414029")
print(r)

"""
    匹配任意（非）数字字符
    元字符: \d \D
    匹配规则:\d 匹配任意数字字符，\D 匹配任意非数字字符
"""
r = re.findall("\d{1,5}", 'port:8888')
print(r)
r = re.findall("\D+", "port:8888")
print(r)

"""
    匹配任意（非）普通字符
    元字符:\w \W
    匹配规则: \w 匹配普通字符，\W 匹配非普通字符
    说明: 普通字符指数字，字母，下划线，汉字。
"""
r = re.findall("\w+", "server_port = 8888")
print(r)

"""
    匹配任意（非）空字符
    元字符:\s \S
    匹配规则:\s 匹配空字符，\S 匹配非空字符
    说明:空字符指 空格 \r \n \t \v \f 字符
"""
r = re.findall("\w+\s+\w+", "hello        world")
print(r)

"""
    匹配（非）单词的边界位置
    元字符: \b \B
    匹配规则: \b 表示单词边界，\B 表示非单词边界
    说明:单词边界指数字字母(汉字)下划线与其他字符的交界位置
"""
r = re.findall(r"\bis", "This is a test")
print(r)
r = re.findall(r"\b[A-Z]+[a-z]*", "Hello and I CBD NBA iPython")
print(r)
