"""
    定义函数,根据年、月、日计算星期。
     0   星期一
     1   星期二
       ....
"""
import time


def get_week(year, month, day):
    str_time = "%d-%d-%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y-%m-%d")
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[time_tuple[6]]


print(get_week(2020, 1, 16))
