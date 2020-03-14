"""
执行两个函数计算执行时间
使用两个进程同时执行这两个事件，再计算时间
"""

import time
import os


def sum():
    result = 0
    for i in range(99999999):
        result += i
    print("hhhhh")


def write_file():
    with open("file.txt", "w") as f:
        for i in range(999999):
            f.write("Hello World\n")


def time_result01():
    r_time = time.time()
    sum()
    write_file()
    print(time.time() - r_time)


def time_result02():
    pid = os.fork()
    if pid == 0:
        print("1")
        r_time = time.time()
        sum()
        print("sum:", time.time() - r_time)
    elif pid < 0:
        return
    else:
        print("2")
        r_time = time.time()
        write_file()
        print("write_file:", time.time() - r_time)


# 顺序执行
time_result01()
time_result02()
