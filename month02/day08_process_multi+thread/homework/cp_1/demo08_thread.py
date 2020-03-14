"""
    Thread
"""
from threading import Thread
from time import sleep
import os

# 线程要做的功能函数
def fun(sec,name):
    print("含有参数的线程")
    sleep(sec)
    print("%s执行完毕"%name)


# 创建多个线程对象
thread_list=[]
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={"name":"T%d"%i})
    t.start()
    thread_list.append(t)
for i in thread_list:
    i.join()

