import numpy as np
a = np.arange(1, 9)  # [1, 2, 3, 4, 5, 6, 7, 8]
b = np.arange(9, 17)  # [9,10,11,12,13,14,15,16]
# 把两个数组摞在一起成两行
c = np.row_stack((a, b))
print(c)
# 把两个数组组合在一起成两列
d = np.column_stack((a, b))
print(d)
