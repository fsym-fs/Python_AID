"""
    群聊聊天室
    功能 ： 类似qq群功能
    【1】 有人进入聊天室需要输入姓名，姓名不能重复
    【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
    【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
    【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
    【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx
"""

from socket import *
import signal
import os
import struct

# 忽略子进程的退出行为
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


class Chat_client:

    def __init__(self):
        self.socket_client = socket(AF_INET, SOCK_DGRAM)
        self.server_addrs = ("192.168.1.6", 8444)
        self.name = "U"
        self.flag = 0
        # self.socket_server.listen(n)

    def main(self):
        while True:
            if self.flag == 0:
                self.flag = self.send_message(1, "姓名")
            else:
                break
        pid = os.fork()
        while True:
            if pid < 0:
                print("Error")
                break
            elif pid == 0:
                print("\n12345678")
                data = self.receive_message()
                print(data.decode())
            else:
                self.send_message(2, "发言")

    def receive_message(self):
        data, addrs = self.socket_client.recvfrom(1024)
        return data

    """
    1 U name
    2 name message
    3 name quite
    """

    def send_message(self, n, msg):
        data = input("请输入" + msg + ":")
        data = str(n) + " " + self.name + " " + data
        self.socket_client.sendto(data.encode(), self.server_addrs)
        if n == 1:
            result = self.receive_message()
            if result.decode() == "OK":
                self.name = data.split(" ", 2)[2]
                print("您已成功加入群聊!")
                return 1
            else:
                print("\nFail")
                return 0
        else:
            print(self.name + ":" + data.split(" ", 2)[2])
            return 2


client = Chat_client()
client.main()
