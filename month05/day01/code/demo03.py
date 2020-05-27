"""
    数据分析
"""
import numpy as np

# 创建ndarray数组
# ary = np.array([[[1,2],[3,4],[5,6],[7,8]]])
a = np.arange(1,9)
print(a,a.shape)
# 页，行，列
a.shape = (2,4)
print(a,a.shape)

# dtype#数据类型
b = np.arange(1,5)
print(b,b.dtype)
# b.dtype = 'float32'
# print(b,b.dtype)
c = b.astype('float32')
print(c,c.dtype)

# size(基层元素个数)
print(a,a.size)

# 索引
print('-'*50)
d = np.arange(1,13)
d.shape = (2,2,3)
print(d, d.shape)
print('-')
print(d[0])
print('-')
print(d[0][0])
print('-')
print(d[0][0][0])
print('-')
print(d[0, 0, 0])
print('-')
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            print(d[i, j, k])
