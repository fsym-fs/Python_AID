"""
时间限制：
    C/C++ 1秒，其他语言2秒 空间限制：C/C++ 32M，其他语言64M 热度指数：1160883
本题知识点:
    链表
题目描述:
    输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        a = []
        l = listNode
        while l:
            a.insert(0,l.val)
            l = l.next
        return a