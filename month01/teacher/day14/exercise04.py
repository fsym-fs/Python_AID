# 定义函数,根据生日(年月日)计算活了多少天。
# 公式：当前时间 - 生日
import time


def life_days(year,month,day):
    str_time = "%d-%d-%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y-%m-%d")
    life_seconds = time.time() - time.mktime(time_tuple)
    return int(life_seconds / 60 / 60 / 24)

print(life_days(1996,4,15))