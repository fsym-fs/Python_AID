"""
    进程池
    **
        父进程结束，进程池自然销毁
        执行的事件函数必须在进程池创建之前声明
        如果用Windows或macos则创建进程必须在main函数中
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件
def wroker(msg):
    sleep(2)
    print(ctime(), "---", msg)


def f():
    print("hhhhh")


# 创建进程池
pool = Pool()

# 向进程池放事件
for i in range(10):
    msg = "GGG%d" % i
    pool.apply_async(func=wroker, args=(msg,))
sleep(3)
# 向进程池再放入事件
pool.apply_async(func=f)
# 关闭进程池，不能再添加新的事件
pool.close()
# 回收进程池
pool.join()
