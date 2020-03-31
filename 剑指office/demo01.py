"""
时间限制：
    C/C++ 1秒，其他语言2秒 空间限制：C/C++ 32M，其他语言64M 热度指数：1521915
本题知识点： 查找 数组
题目描述:
    在一个二维数组中（每个一维数组的长度相同），
    每一行都按照从左到右递增的顺序排序，
    每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
# -*- coding:utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            if array[i][0] >= target:
                if target in array[i]:
                    return 'true'
        return 'false'


for i in range(len(array)):
            if target in array[i]:
                return 'true'
        return 'false'

while True:
    try:
        S = Solution()
        # 字符串转为list
        L = list(eval(input()))
        array = L[1]
        target = L[0]
        print(S.Find(target, array))
    except:
        break
