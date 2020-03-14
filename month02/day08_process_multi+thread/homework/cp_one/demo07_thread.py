"""
    Thread
"""
from threading import Thread
from time import sleep
import os

a = 1


# 线程要做的功能函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放第%d首歌曲" % i)
    global a
    a = 1000


# 创建线程对象
t = Thread(target=music)

print("a:", a)
# 启动线程
t.start()

# 主线程
print("主线程")
for i in range(4):
    sleep(1)
    print(os.getpid(), "播放%d。。。" % i)

# 回收线程
t.join()
print("a:", a)
