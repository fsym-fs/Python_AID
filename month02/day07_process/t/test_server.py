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


class Chat_server:
    def __init__(self):
        # {name:addrs}
        self.client_dict = {}
        self.socket_server = socket(AF_INET, SOCK_DGRAM)
        self.socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        self.server_addrs = ("192.168.1.6", 8444)
        self.socket_server.bind(self.server_addrs)

    def main(self):
        print("等待链接......")
        while True:
            data, addr = self.receive_message()
            msg = data.decode().split(" ", 2)
            if msg[0] == "1":
                if msg[2] in self.client_dict:
                    self.send_message(1, msg[1], "Not", addr)
                else:
                    ms = "\n欢迎" + msg[2] + "加入群聊!"
                    self.send_message(2, msg[2], ms, addr)
            if msg[0] == "2":
                ms = "\n" + msg[1] + ":" + msg[2]
                self.send_message(3, msg[1], ms, addr)

    def receive_message(self):
        data, addrs = self.socket_server.recvfrom(1024)
        return (data, addrs)

    def send_message(self, n, name, msg, addr):
        if n == 1:
            self.socket_server.sendto(msg.encode(), addr)
        else:
            for i in self.client_dict:
                if i != name:
                    self.socket_server.sendto(msg.encode(), self.client_dict[i])
            if n == 2:
                self.socket_server.sendto(b"OK", addr)
            self.client_dict[name] = addr


server = Chat_server()
server.main()
