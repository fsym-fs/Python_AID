from socket import *


class Client_Controls:
    def __init__(self):
        ADDR = ("192.168.1.4", 8844)
        self.c = socket()
        self.c.connect(ADDR)
        self.name = ""

    # 登录
    def login(self):
        name = input("请输入您的用户名:")
        password1 = input("请输入您的密码:")
        password2 = input("请确认您的密码:")
        if password2 == password1:
            msg = "L " + name + " " + password1
            self.c.send(msg.encode())
        else:
            print("两次密码不相同,请重新输入!")
            return False
        data = self.c.recv(128).decode()
        if data == "OK":
            self.name = name
            return True
        else:
            return False

    # 注册
    def register(self):
        name = input("请输入您的用户名:")
        password1 = input("请输入您的密码:")
        password2 = input("请确认您的密码:")
        if password2 == password1:
            msg = "R " + name + " " + password1
            self.c.send(msg.encode())
        else:
            print("两次密码不相同,请重新输入!")
            return False
        data = self.c.recv(128).decode()
        if data == "OK":
            return True
        else:
            return False

    # 退出
    def do_exit(self):
        msg = "E exit exit"
        self.c.send(msg.encode())
        data = self.c.recv(128).decode()
        if data == "OK":
            return True
        else:
            return False

    # 查询单词
    def find_words(self):
        word = input("请输入您要查询的单词:")
        if word == "##":
            return "out"
        msg = "F " + self.name + " " + word
        self.c.send(msg.encode())
        data = self.c.recv(128).decode()
        print(data)

    # 查看历史记录
    def history(self):
        msg = "H " + self.name + " word"
        self.c.send(msg.encode())
        while True:
            data = self.c.recv(1024).decode()
            if data != "#":
                print(data, end="")
            else:
                break
