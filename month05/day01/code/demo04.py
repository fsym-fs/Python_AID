"""
    数据分析
"""
# 自定义复合类型
import numpy as np

data = [
    ('zs', [90, 80, 85], 15),
    ('ls', [92, 81, 83], 16),
    ('ww', [95, 85, 95], 15)
]
# 第一种设置dtype的方式
a = np.array(data, dtype='U3, 3int32, int32')
print(a)
print(a[0]['f0'], ":", a[1]['f1'])
print("=====================================")
# 第二种设置dtype的方式
b = np.array(data, dtype=[('name', 'str_', 2),
                          ('scores', 'int32', 3),
                          ('ages', 'int32', 1)])
print(b[0]['name'], ":", b[0]['scores'])
print("=====================================")

# 第三种设置dtype的方式
c = np.array(data, dtype={'names': ['name', 'scores', 'ages'],
                          'formats': ['U3', '3int32', 'int32']})
print(c[0]['name'], ":", c[0]['scores'], ":", c.itemsize)
print("=====================================")

# 第四种设置dtype的方式
# 16为开始地址
d = np.array(data, dtype={'names': ('U3', 0),
                          'scores': ('3int32', 16),
                          'ages': ('int32', 28)})
print(d[0]['names'], d[0]['scores'], d.itemsize)

print("=====================================")

# 测试日期类型数组
f = np.array(['2011', '2012-01-01', '2013-01-01 01:01:01', '2011-02-01'])
# 精确到天的日期时间
f = f.astype('datetime64[D]')
print(f,f.dtype)
f = f.astype('M8[D]')
print(f,f.dtype)
# f = f.astype('int32')
# print(f,f.dtype)
print(f[3] - f[0])
