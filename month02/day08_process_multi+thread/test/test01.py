"""
    在不改变函数的定义与调用基础上,为其增加新功能(执行时间)
"""
import time
from multiprocessing import Process


def account_time(func):
    def wapper(*args, **kwargs):
        time01 = time.time()
        result = func(*args, **kwargs)
        time02 = time.time() - time01
        print(time02)
        return result

    return wapper


def account(n1, n2):
    print("start")
    list01 = []
    flog = 1
    for i in range(n1, n2):
        for j in range(2, i):
            if i % j == 0:
                flog = 0
                break
    print("end")


@account_time  # ===>func01 = account(func01)
def func01():
    account(1, 100001)


@account_time
def func02(n1, n2):
    list01 = []
    n = n1 // n2
    print(n)
    list01.append(Process(target=account, args=(1, n)))
    for i in range(1, n2):
        list01.append(Process(target=account, args=(n * i, n * (i + 1))))
    for i in list01:
        i.start()
    for i in list01:
        i.join()


# func01()
func02(100000, 4)
