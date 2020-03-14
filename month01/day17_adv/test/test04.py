"""
    在不改变函数的定义与调用基础上,为其增加新功能(执行时间)
"""
import time


def account_time(func):
    def wapper(*args, **kwargs):
        time01 = time.time()
        result = func(*args, **kwargs)
        time02 = time.time() - time01
        print(time02)
        return result

    return wapper


@account_time  # ===>func01 = account(func01)
def func01():
    for _ in range(10):
        pass


@account_time
def func02():
    for _ in range(1000000000):
        pass


func01()
func02()
