"""
创建监听套接字
循环接收客户端连接请求
当有新的客户端连接创建线程处理客户端请求
主线程继续等待其他客户端连接
当客户端退出，则对应分支线程退出
"""
from socket import *
from threading import Thread, Lock

HOST = "192.168.1.6"
POST = 8844
ADDR = (HOST, POST)


# 处理客户端请求函数
def use(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(4)
print("Listen the port 8844")

while True:
    c, addr = s.accept()
    print("Connect from", addr)
    t = Thread(target=use, args=(c,))
    t.setDaemon(True)
    t.start()
    # t.join()

s.close()

# list01=[]
# for i in range(10):
#     t = Thread()
#     t.start()
#     list01.append(t)
# for i in list01:
#     i.jion()
