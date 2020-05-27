"""
    数据分析
"""
import numpy as np

# 创建ndarray数组
ary = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(ary)

b = np.arange(1,10,2)
print(b)

c = np.zeros(10,dtype='int32')
print(c)

d = np.ones((2,4),dtype='int32')
print(d)

# zeros_like()   ones_like()
e = np.zeros_like(d)
print(e)