"""
    数据分析
    切片
"""

import numpy as np

a = np.arange(1, 28)
a.resize(3, 3, 3)
print(a)
# 切出1页
print(a[1, :, :])
# 切出所有页的1行
print(a[:, 1, :])
# 切出0页的1行1列
print(a[0, :, 1])

b = np.arange(1, 10)
mask = [True, False,True, False,True, False,True, False,True, False]
print(b[mask])
