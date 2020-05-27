"""
    数据分析
"""
import numpy as np

# 创建ndarray数组
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary))

print(ary + 3)
# [4 5 6 7 8 9]
print(ary + ary)
# [ 2  4  6  8 10 12]
print(ary * 2)
#  2  4  6  8 10 12]
print(ary > 3)
# [False False False  True  True  True]

ary = np.array([[1,2,3],[4,5,6]])
print(ary)
"""
    [[1 2 3]
     [4 5 6]]
"""