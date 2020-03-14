"""
    基于fork的多进程并发
    步骤：
        创建监听套接字
        等待接收客户端请求
        客户端连接创建新的进程处理客户端请求
        原进程继续等待其他客户端连接
        如果客户端退出，则销毁对应的进程
"""
import os
from socket import *
import signal

# 全局变量
HOST = "192.168.1.6"
POST = 8844
ADDR = (HOST, POST)


# 处理客户端请求函数
def handle(c, addr):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()


# 创建监听套接字
s = socket()

# 端口立即重用 (在bind之前)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(ADDR)
s.listen(3)

print("Listen the port 8844")

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 循环等待客户端链接
while True:
    c, addr = s.accept()
    print("Connect from", addr)

    # 创建一个新的进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        # 处理客户端请求

        # 处理客户端请求函数
        handle(c, addr)

        # 子进程处理完客户端请求则退出
        os._exit(0)
    else:
        # 出错或者父进程都继续等待接受客户端链接
        continue

# 服务端退出
s.close()
