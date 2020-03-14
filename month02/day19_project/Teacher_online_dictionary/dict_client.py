"""
客户端 ： 发起请求获取结果
"""
from socket import *
import sys

# 全局变量 服务器地址
ADDR = ('127.0.0.1', 8000)
User_name = ""


# 二级界面
def second(s, name):
    while True:
        print("===============Query===============")
        print("1. 查单词    2. 历史记录   3.注销")
        print("===================================")
        cmd = input("输入命令：")
        if cmd == '1':
            do_query(s, name)
        elif cmd == '2':
            do_history(s, name)
        elif cmd == '3':
            break


# 注册功能
def do_register(s):
    name = input("Name:")
    passwd = input('Password:')
    # 发送请求
    msg = "R %s %s" % (name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()  # 等待结果
    if data == 'OK':
        print("注册成功")
    else:
        print("注册失败")


# 登录功能
def do_login(s):
    name = input("Name:")
    passwd = input('Password:')
    # 发送请求
    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()  # 等待结果
    if data == 'OK':
        print("登录成功")
        second(s, name)
    else:
        print("登录失败")


# 退出功能
def do_exit(s):
    # 发送请求
    msg = "E"
    s.send(msg.encode())
    data = s.recv(128).decode()  # 等待结果
    if data == 'OK':
        print("退出成功")
        exit()
    else:
        print("退出失败")


# 查单词
def do_query(s, name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q " + word + " " + name
        s.send(msg.encode())
        data = s.recv(1024).decode()
        print(data)


# 查询历史记录
def do_history(s, name):
    msg = "H " + name
    s.send(msg.encode())
    while True:
        data = s.recv(1024).decode()
        if data != "#":
            print(data, end="")
        else:
            break


# 链接服务器
def main():
    s = socket()
    s.connect(ADDR)  # 发起链接

    # 一级界面
    while True:
        print("=============Welcome==============")
        print("1. 注册     2. 登录       3.退出")
        print("==================================")
        cmd = input("输入命令：")
        if cmd == '1':
            do_register(s)
        elif cmd == '2':
            do_login(s)
        elif cmd == '3':
            do_exit(s)


if __name__ == '__main__':
    main()
