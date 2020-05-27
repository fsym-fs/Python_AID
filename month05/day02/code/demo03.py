import pandas as pd

import numpy as np

# test
ary = np.array(['张三','李四','王五','赵柳'])
s = pd.Series(ary,index=['s01','s02','s03','s04'])
print(s,type(s))
print(s['s01'],s[0])

# 从字典创建一个Series
data = {'100' : '张三', '101' : '李四', '102' : '王五'}
s = pd.Series(data)
# 从标量创建一个Series
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01',
                   '2011/05/01 01:01:01', '01 Jun 2011'])
# to_datetime() 转换日期数据类型
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
# 获取时间的某个日历字段的数值
print(dates.dt.day)