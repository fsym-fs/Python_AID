"""
    有两个线程，同时运行
    1个线程打印1-52这52个数字
    另一个线程打印A-Z这26个字母
    希望通过互斥机制的控制，让打印结果为12A34B56C......5152Z
"""

from threading import Thread, Lock

lock01 = Lock()
lock02 = Lock()


def print_A_Z():
    for x in range(ord('A'), ord('Z') + 1):
        lock02.acquire()
        print(chr(x), end="")
        lock01.release()


def print_1_52():
    for i in range(1, 53, 2):
        lock01.acquire()
        print(i, end="")
        print(i + 1, end="")
        lock02.release()


t1 = Thread(target=print_1_52)
t2 = Thread(target=print_A_Z)
lock02.acquire()
t1.start()
t2.start()
t1.join()
t2.join()
