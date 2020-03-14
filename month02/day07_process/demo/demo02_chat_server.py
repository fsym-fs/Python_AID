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
import os
import signal

# 忽略子进程的退出行为
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 全局变量
ADDR = ("0.0.0.0", 8888)
# 用户列表{name:address}
user = {}


# 进入聊天室
def do_login(s, name, addr):
    if name in user or "管理" in name:
        s.sendto(b"Fail", addr)
        return
    else:
        s.sendto(b"OK", addr)
    msg = "\n" + name + "进入聊天室.."
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr


# 转发聊天信息
# C name msg
def do_chat(s, name, content):
    msg = "\n%s:%s" % (name, content)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


def do_send_mes(s, name, msg, addr):
    msg = "name" + ":" + msg
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
    s.sendto(b"OK", addr)


# 退出
def do_quit(s, name):
    msg = "\n" + name + "退出聊天室"
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b"EXIT", user[i])
    del user[name]


# 基本结构(接受请求，分配任务)
def main():
    # udp服务套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    s.bind(ADDR)
    pid = os.fork()
    if pid < 0:
        print("Error")
    elif pid == 0:
        content = input("管理员消息:")
        msg = "C %s %s"%("管理员消息:",content)
        s.sendto(msg.encode(),ADDR)
    else:
        while True:
            data, addr = s.recvfrom(1024)
            # print("接收到的请求内容：", data.decode())
            # 对请求内容进行解析
            tmp = data.decode().split(" ", 2)
            if tmp[0] == "L":
                do_login(s, tmp[1], addr)
            elif tmp[0] == "C":
                do_chat(s, tmp[1], tmp[2])
                # do_send_mes(s, tmp[1], tmp[2], addr)
            elif tmp[0] == "Q":
                do_quit(s, tmp[1])
            else:
                pass


if __name__ == '__main__':
    main()
