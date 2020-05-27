""""
    数据分析
"""
import numpy as np
n = (1,2,3,4,5,6)
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary,n)
print(type(ary),type(n))

# 多于一个维度
import numpy as np
a = np.array([[1,  2],  [3,  4],[5,6]])
b = [[1,  2],  [3,  4],[5,6]]
# print(b)
print(a)

# 最小维度
import numpy as np
a = np.array([1,  2,  3,4,5], ndmin =  2)
print(a)