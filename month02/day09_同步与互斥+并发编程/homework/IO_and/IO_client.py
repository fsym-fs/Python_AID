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


class Io_client:
    def __init__(self):
        # 处理僵尸进程
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        self.client = socket()
        self.client.connect(("192.168.1.6", 8844))
        self.func_list = [self.func1, self.func2, self.func3, self.func4]

    def use(self):
        show_input = self.client.recv(1024)
        while True:
            print(show_input.decode())
            n = input("请输入您要进入的功能:")
            if not n:
                print("即将退出......")
                break
            else:
                self.client.send(n.encode())
                data = self.client.recv(1024)
                if data.decode() == "OK":
                    self.func_list[int(n) - 1]()
                else:
                    print(data.decode())
        self.client.close()

    # 可以查看服务器文件库中有什么文件
    def func1(self):
        data = self.client.recv(1024)
        print(data.decode())

    # 从文件库中下载文件到本地
    def func2(self):
        file_name = input("输入你要下载的文件的名字:")
        file_path = "client_file/" + file_name
        self.client.send(file_name.encode())
        file_data = self.client.recv(1024)
        if file_data.decode() == "Not":
            print("没有该文件!")
            return
        else:
            print("开始下载")
            with open(file_path, "wb", 1) as f:
                while True:
                    file_data = self.client.recv(1024)
                    if file_data == b"_OK_":
                        print("下载完成!")
                        return
                    else:
                        f.write(file_data)

    # 上传一个本地文件到文件库
    def func3(self):
        file_list = os.listdir("client_file")
        print(file_list)
        file_name = input("输入你要上传的文件的名字:")
        file_path = "client_file/" + file_name
        self.client.send(file_name.encode())
        if os.path.exists(file_path):
            if self.client.recv(1024) == b"_OK_":
                with open(file_path, "rb") as f:
                    data = f.readline()
                    self.client.send(data)
                    while True:
                        data = f.readline()
                        if data:
                            self.client.send(data)
                        else:
                            time.sleep(0.1)
                            self.client.send(b"_OK_")
                            print("上传完成")
                            break
        else:
            print("没有该文件!")

    # 退出服务器
    def func4(self):
        print("即将退出.....")
        self.client.close()
        os._exit(0)


def main():
    i_s = Io_client()
    i_s.use()


if __name__ == '__main__':
    main()
