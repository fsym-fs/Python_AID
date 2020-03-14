"""
fork进程
"""
import os
from time import sleep

print("====================")
a = 1
pid = os.fork()
if pid < 0:
    print("创建进程失败！")
elif pid == 0:
    a = 100
    print("a=", a)
    print("新的进程")
else:
    print("a=", a)
    print("原来的进程")
print("实验完毕")
