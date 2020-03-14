"""
    作业：
        1. 并发模型自己会写
        2. 分析文件服务器模型，尝试编写其中的功能

    功能:
    【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
    【2】 客户端可以查看服务器文件库中有什么文件。
    【3】 客户端可以从文件库中下载文件到本地。
    【4】 客户端可以上传一个本地文件到文件库。
    【5】 使用print在客户端打印命令输入提示，引导操作
"""

from socket import *
# from multiprocessing import Process
import os
import signal
import time


class Io_server:
    def __init__(self):
        # 处理僵尸进程
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        self.server = socket()
        # 端口立即重用 (在bind之前)
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server.bind(("192.168.1.6", 8844))
        self.server.listen(4)
        self.func_list = [self.func1, self.func2, self.func3, self.func4]

    def main(self):
        while True:
            print("等待客户端链接.......")
            c, addr = self.server.accept()
            # print("c", c)
            pid = os.fork()
            if pid == 0:
                self.use(c, addr)
                os._exit(0)
            else:
                continue
            # p = Process(target=self.use, args=(c, addr))
            # p.start()

    def use(self, c, addr):
        show_input = """
**************************
1.查看服务器文件库中所有文件
2.从文件库中下载文件到本地
3.上传一个本地文件到文件库
4.退出服务器
    
    欢迎光临浮生@服务器
**************************
        """
        c.send(show_input.encode())
        while True:
            data = c.recv(1024)
            # print(data.decode())
            if not data:
                break
            else:
                try:
                    if int(data.decode()) > len(self.func_list):
                        c.send("输入错误,请重新输入".encode())
                    else:
                        c.send("OK".encode())
                        # time.sleep(1)
                        self.func_list[int(data.decode()) - 1](c)
                except:
                    c.send("输入错误,请重新输入".encode())
        c.close()

    # 可以查看服务器文件库中有什么文件
    def func1(self, c):
        file_list = os.listdir("server_file")
        file_list_str = str(file_list)
        c.send(file_list_str.encode())

    # 从文件库中下载文件到本地
    def func2(self, c):
        file_name = c.recv(1024)
        file_name = file_name.decode()
        file_path = "server_file/" + file_name
        print(file_path)
        if os.path.exists(file_path):
            c.send(b"_Start_")
            time.sleep(0.1)
            with open(file_path, "rb") as f:
                while True:
                    data = f.readline()
                    if data:
                        c.send(data)
                    else:
                        time.sleep(0.1)
                        c.send(b"_OK_")
                        break
        else:
            c.send(b"Not")

    # 上传一个本地文件到文件库
    def func3(self, c):
        data = c.recv(1024)
        file_path = "server_file/" + data.decode()
        c.send(b"_OK_")
        with open(file_path, "wb", 1) as f:
            while True:
                file_data = c.recv(1024)
                if file_data == b"_OK_":
                    return
                else:
                    f.write(file_data)

    # 退出服务器
    def func4(self, c):
        c.close()
        os._exit(0)


def main():
    i_s = Io_server()
    i_s.main()


if __name__ == '__main__':
    main()
