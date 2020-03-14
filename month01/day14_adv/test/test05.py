"""
    time
    定义函数:根据年,月,日计算星期:
            星期一
            星期二
            .
            .
            .
"""
import time
def result_time(year,month,day):
    list01=("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    s1 = time.strptime("%d,%d,%d"%(year,month,day),"%Y,%m,%d")
    s2 = s1.tm_wday
    print(list01[s2])
    # if s2 == 1:
    #     print("星期一")
    # elif s2 == 2:
    #     print("星期二")
    # elif s2 == 3:
    #     print("星期三")
    # elif s2 == 4:
    #     print("星期四")
    # elif s2 == 5:
    #     print("星期五")
    # elif s2 == 6:
    #     print("星期六")
    # elif s2 == 7:
    #     print("星期日")
    # else:
    #     pass
result_time(2020,1,22)