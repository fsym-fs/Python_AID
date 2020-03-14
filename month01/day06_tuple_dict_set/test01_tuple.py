"""
Test01_tuple
    获取 年,月,日
    计算这是这一年的第几天
"""
year = int(input("输入一个年份:"))
month = int(input("输入一个月份:"))
day = int(input("输入一个日期:"))
month_list = (4, 6, 9, 11)
s = 0
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    m = 29
else:
    m = 28
for i in range(1, month, 1):
    if i == 2:
        s += m
    elif i in month_list:
        s += 30
    else:
        s += 31
s += day
print(s)
