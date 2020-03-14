"""
    群聊聊天室
    功能 ： 类似qq群功能
    【1】 有人进入聊天室需要输入姓名，姓名不能重复
    【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
    【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
    【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
    【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx
"""
"""
"""
from socket import *
import os, sys
import signal

# 忽略子进程的退出行为
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 服务端地址
ADDR = ("127.0.0.1", 8888)


# 群聊发送信息
def send_msg(s, name):
    while True:
        try:
            content = input("发言:")
        except:
            content = "quit"
        if content == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("谢谢使用!")
        msg = "C %s %s" % (name, content)
        s.sendto(msg.encode(), ADDR)


def do_send(s, name):
    while True:
        msg = input(name + ":")
        if not msg:
            break
        msg = "C" + " " + name + " " + msg
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print(name, ":", msg.split(" ", 2)[2])


# 群聊接收信息
def recv_msg(s):
    while True:
        data, addr = s.recvfrom(1024)
        if data.decode()=="EXIT":
            sys.exit()
        print(data.decode()+"\n发言:",end="")


def do_rec(s):
    while True:
        data, addr = s.recvfrom(1024)
        print(data.decode())


# 启动函数--->向服务端发送初始请求
def main():
    # udp客户端
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(b"request", ADDR)
    while True:
        """
        自定义通信协议
            L name
            C
            Q
        """
        name = input("请输入您的用户名:")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室!")
            break
        else:
            print("进入失败!")
    pid = os.fork()
    if pid < 0:
        print("Error")
        return
    elif pid == 0:
        recv_msg()
        # do_rec(s)
    else:
        send_msg(s, name)
        # do_send(s, name)


if __name__ == '__main__':
    main()
