"""
    multiprocessing模块
        【1】 将需要子进程执行的事件封装为函数
        【2】 通过模块的Process类创建进程对象，关联函数
        【3】 可以通过进程对象设置进程信息及属性
        【4】 通过进程对象调用start启动进程
        【5】 通过进程对象调用join回收进程

    (
    注意:
        1.如果用Windows或macos则创建进程必须在main函数中
            if __name__ == '__main__':
                main()
        2.multiprocessing创建的进程不可以用input方法
    )

"""

import multiprocessing
from time import sleep

a = 1


# 创建执行函数
def fun():
    print("开始一个进程")
    sleep(5)
    print("a:", a)
    print("子进程执行结束")


# 创建进程对象
p = multiprocessing.Process(target=fun, name="hh")

# 进程名字
print(p.name)
p.name = "tt"
print(p.name)

# 设置父子进程的退出关系
p.daemon = True

# 启动进程
p.start()

# 查看子进程的生命周期
print(p.is_alive())

# 查看子进程的进程id
print(p.pid)

# 父进程
sleep(3)
print("父进程")

# 回收进程,防止僵尸进程
# p.join()
print("==================================")
