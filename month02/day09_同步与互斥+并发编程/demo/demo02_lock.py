"""
    线程同步互斥之线程锁 Lock
    注意:
        每个需要使用共享资源的线程都需要进行上锁和解锁
"""
from threading import Thread, Lock

a = b = 0
# 创建线程锁对象
lock = Lock()


# 线程函数
def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d" % (a, b))
        lock.release()


t = Thread(target=value)
t.daemon = True
t.start()

while True:
    # lock.acquire()
    # a += 1
    # b += 1
    # lock.release()
    with lock:
        a += 1
        b += 1

# t.join()
