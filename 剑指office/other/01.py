# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        result = "false"
        i = len(array)
        j = len(array[0])
        for m in range(0, i):
            if target in array[m]:
                result = "true"
                break
        print(result)


s = Solution()
a = [[1, 2, 8, 9], [4, 7, 10, 13]]
s.Find(7, a)
