"""
时间限制：
    C/C++ 1秒，其他语言2秒 空间限制：C/C++ 32M，其他语言64M 热度指数：1294294
本题知识点： 字符串
题目描述:
    请实现一个函数，将一个字符串中的每个空格替换成“%20”。
    例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ',"%20")
while True:
    try:
        f = Solution()
        array = input()
        print(f.replaceSpace(array))
    except :
        break
