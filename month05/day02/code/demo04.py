import pandas as pd

data = {'zs':85,'ls':95,'ww':90,'zl':83}

s = pd.Series(data)
print(s)
print(s.values)
print(s.index)

# 日期
# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01',
                   '2011/05/01 01:01:01', '01 Jun 2011'])
# to_datetime() 转换日期数据类型
# 精确到纳秒,输出到秒
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
# 获取时间的某个日历字段的数值
delta = dates - pd.to_datetime('2011.1.1')
print(delta)
# 获取时间的某个日历字段的数值
print(dates.dt.day)
# 把时间偏移量换算成天数
print(delta.dt.days)

# 以日为频率,生成一组日期序列
datelist = pd.date_range('2019/08/21', periods=5)
print(datelist)
# 以月为频率
datelist = pd.date_range('2019/08/21', periods=5,freq='M')
print(datelist)
# 构建某个区间的时间序列
# 字符串也可
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
dates = pd.date_range(start, end)
print(dates)