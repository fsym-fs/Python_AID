"""
    数据分析
    掩码
"""
import numpy as np

a = np.arange(1, 10)
mask = a % 2 == 0
# print(mask)
# mask = [True, False, True, False, True, False, True, False, True, False]
print(a[mask])

a = np.arange(100)
print(a[(a % 7 == 0) & (a % 3 == 0)])

products = np.array(['Apple','Mi','Huawei','Oppo'])
inds = [1,3,2,0]
# print(inds)
# print(products)
# ['Mi' 'Oppo' 'Huawei' 'Apple']
print(products[inds])
