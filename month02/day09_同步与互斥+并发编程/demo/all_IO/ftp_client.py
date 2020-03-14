"""
    ftp_client
    【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
    【2】 客户端可以查看服务器文件库中有什么文件。
    【3】 客户端可以从文件库中下载文件到本地。
    【4】 客户端可以上传一个本地文件到文件库。
    【5】 使用print在客户端打印命令输入提示，引导操作
"""
from socket import socket
import os, sys
from time import sleep

# 全局变量
ADDR = ("127.0.0.1", 8845)
FTP = "Use/"


class FTPClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def quit(self):
        self.sockfd.send(b'E')
        self.sockfd.close()
        sys.exit("谢谢使用!")

    def list(self):
        self.sockfd.send(b'L')
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 接收文件
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            # 打印原因
            print(data)

    def get_file(self, file_name):
        data = "G " + file_name
        # 下载文件    G              filename
        self.sockfd.send(data.encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            # 接收文件
            f = open(FTP + file_name, "wb")
            while True:
                data = self.sockfd.recv(1024)
                # print(data)
                # 文件接收完毕的标志
                if data == b"##":
                    print("OK")
                    break
                f.write(data)
            f.close()

    # 上传文件
    def put(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except:
            print("文件不存在")
            return
        data = "P " + filename
        self.sockfd.send(data.encode())  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')  # 结束标志
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


# 启动函数
def main():
    # 链接服务端
    s = socket()
    s.connect(ADDR)

    # 实例化对象，用于调用类中的方法，实现与服务端的交互
    ftp = FTPClient(s)

    # 循环发送请求
    while True:
        print("===============命令选项===============")
        print("***             list              ***")
        print("***           get file            ***")
        print("***           put file            ***")
        print("***             quit              ***")
        print("=====================================")
        cmd = input("输入命令:")
        # s.send(cmd.encode())
        if cmd == 'quit':
            ftp.quit()
        elif cmd == 'list':
            ftp.list()
        elif cmd[:3] == 'get':
            file_name = cmd.split(" ", 1)[-1]
            ftp.get_file(file_name)
        elif cmd[:3] == 'put':
            file_name = cmd.split(" ", 1)[-1]
            ftp.put(file_name)
        else:
            pass


if __name__ == '__main__':
    main()
