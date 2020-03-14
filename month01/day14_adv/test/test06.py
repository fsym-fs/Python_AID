"""
    time
    定义函数:根据生日(年,月,日)计算活了多少天:
            .
            .
            .
"""
import time
def get_days(year,month,day):
    time1 = time.time()
    time2 = time.strptime("%d,%d,%d"%(year,month,day),"%Y,%m,%d")
    time2 = time.mktime(time2)
    d = (int(time1)-time2)//60//60//24
    print(str(int(d))+"天")
get_days(2020,1,14)
