"""
    数据分析
"""
# import numpy as np
#
# a = np.arange(1, 7).reshape(2, 3)
# b = np.arange(7, 13).reshape(2, 3)
# # 垂直方向完成组合操作，生成新数组
# c = np.vstack((a, b))
# # 垂直方向完成拆分操作，生成两个数组
# d, e = np.vsplit(c, 2)
#
# print(a)
# print('-' * 50)
# print(b)
# print('-' * 50)
# print(c)


# import numpy as np
# a = np.arange(1, 7).reshape(2, 3)
# b = np.arange(7, 13).reshape(2, 3)
# # 水平方向完成组合操作，生成新数组
# c = np.hstack((a, b))
# # 水平方向完成拆分操作，生成两个数组
# d, e = np.hsplit(c, 2)
# print(c)
# print(d,e,sep='\n')

import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 深度方向（3维）完成组合操作，生成新数组
print(a)
print(b)
i = np.dstack((a, b))
print(i)
# 深度方向（3维）完成拆分操作，生成两个数组
k, l = np.dsplit(i, 2)