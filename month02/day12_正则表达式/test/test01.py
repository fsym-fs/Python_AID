"""
    1.匹配密码:数字字母下划线构成 8--12位
    2.匹配数字:正数 负数 百分数(23%)
    3.匹配大写字母开头的单词 Hello and I CBD NBA
"""
import re

# 匹配密码:数字字母下划线构成 8--12位
r = re.findall("[_0-9a-zA-Z]{8,12}", "223751_ab99")
print(r)
# 匹配数字:正数 负数 百分数(23%)
r = re.findall("-?[0-9]+%?", "10 -5 50 23%")
print(r)

# 匹配大写字母开头的单词 Hello and I CBD NBA
r = re.findall(r"\b[A-Z]+[a-z]*", "Hello and I CBD NBA iPython")
print(r)

