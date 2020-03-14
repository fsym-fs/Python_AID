"""
FTP 文件处理
多线程并发和套接字练习
"""

from socket import *
from threading import Thread
import os
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8845
ADDR = (HOST, PORT)
# 文件库
FTP = "FTP/"


# 处理客户端请求 (自定义线程类)
class FTPServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()
        self.dict_func = {"E": self.f4, "L": self.f1, "P": self.f2, "G": self.f3}

    #  循环接收请求，分发任务
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()  # 接收请求
            print(data)
            if not data or data == 'E':
                # run函数结束对应线程结束
                break
            elif data == 'L':
                self.list()
            elif data[0] == 'G':
                self.get_file(data.split(" ", 1)[-1])
            elif data[0] == 'P':
                self.put(data.split(" ", 1)[-1])

    # 查看文件
    def list(self):
        # 判断文件库是否为空
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)

        # 发送文件列表
        # 讲文件列表以‘\n’拼接，进行添加消息边界以处理沾包
        data = '\n'.join(file_list)
        self.connfd.send(data.encode())

    # 下载文件
    def get_file(self, file_name):
        file_path = FTP + file_name
        try:
            f = open(file_path, "rb")
        except:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
        f.close()

    # 处理上传
    def put(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        # 循环接收文件写入本地
        f = open(FTP + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            # 文件接收完毕的标志
            if data == b'##':
                break
            f.write(data)
        f.close()


# 框架结构，启动函数
def main():
    # 创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port 8845")

    # 循环等待客户端链接
    while True:
        c, addr = s.accept()
        print("Connect from", addr)

        # 创建线程处理客户端请求
        t = FTPServer(c)  # 通过自定义线程类创建线程
        t.setDaemon(True)  # 分支线程随主线程退出
        t.start()

    s.close()


if __name__ == '__main__':
    main()
