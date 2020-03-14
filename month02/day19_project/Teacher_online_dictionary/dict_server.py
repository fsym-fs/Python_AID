"""
服务端
逻辑处理
"""

from socket import *
from multiprocessing import Process
import signal, sys, os
from dict_db import Database
import time

# 定义地址为全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)

# 实例化一个对象帮助处理数据库交互的工作 (链接数据库)
db = Database()


# 注册处理函数
def do_register(connfd, name, passwd):
    # 调用数据处理方法判定可否注册
    if db.register(name, passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'FAIL')


# 登录处理函数
def do_login(connfd, name, passwd):
    # 调用数据处理方法判定可否登录
    if db.login(name, passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'FAIL')


# 退出处理函数
def do_exit(connfd):
    connfd.send(b'OK')
    sys.exit("当前客户端已退出!")


# 查单词
def do_query(connfd, word, name):
    mean = db.query(word, name)
    msg = "%s : %s" % (word, mean)
    connfd.send(msg.encode())


# 查询历史记录
def do_history(connfd, name):
    history_tuple = db.history(name)
    if history_tuple:
        for i in history_tuple:
            msg = str(i[0]) + " " + str(i[1]) + ":" + str(i[2]) + "\n"
            connfd.send(msg.encode())
    else:
        connfd.send("该用户没有历史记录....\n".encode())
    time.sleep(0.1)
    connfd.send(b"#")


# 处理客户端请求
def handle(connfd):
    db.create_cursor()  # 每个进程创建各自的游标
    while True:
        data = connfd.recv(1024).decode()  # 接收请求
        tmp = data.split(' ')
        if not tmp or tmp[0] == 'E':
            do_exit(connfd)
            return
        elif tmp[0] == 'R':
            # "R name password"
            do_register(connfd, tmp[1], tmp[2])
        elif tmp[0] == 'L':
            do_login(connfd, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            do_query(connfd, tmp[1], tmp[2])
        elif tmp[0] == 'H':
            do_history(connfd, tmp[1])
        else:
            pass


# 创建多进程并发模型
def main():
    # 创建套接字
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    print("Listen the port 8000")
    while True:
        # 等待客户端链接
        c, addr = s.accept()
        print("Connect from", addr)

        # 为每个客户端创建进程
        p = Process(target=handle, args=(c,))
        p.start()


if __name__ == '__main__':
    main()
