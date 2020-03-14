"""
    非阻塞IO演示
"""
from socket import socket
from time import sleep, ctime

# 创建tcp套接字
sockfd = socket()
sockfd.bind(("127.0.0.1", 8845))
sockfd.listen(3)

# 将套接字设置为非阻塞

# sockfd.setblocking(False)

# 设置套接字超时检测
sockfd.settimeout(2)

f = open("test.log", "a")
while True:
    print("等待客户端链接......")
    try:
        c, addr = sockfd.accept()
        print("From", addr)
    except Exception:

        # 做其他和链接客户端无关的事
        # print(Exception)
        sleep(2)
        msg = "%s:%s\n" % (ctime(), Exception)
        f.write(msg)
        f.flush()
    else:
        data = sockfd.recv(1024)
