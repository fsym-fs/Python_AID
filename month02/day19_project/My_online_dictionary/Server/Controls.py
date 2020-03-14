from socket import *
from multiprocessing import Process
import signal
from Server.Models import Server_Models
import time


class Server_Controls:
    def __init__(self, host="192.168.1.4", post=8844, db_host='localhost', port=3306, user="hhh",
                 password="223751093",
                 database="dict",
                 charset="utf8"):
        self.host = host
        self.post = post
        self.db = Server_Models(db_host, port, user, password, database, charset)
        self.server = socket()
        self.server.bind((self.host, self.post))
        self.server.listen(4)
        # 处理僵尸进程
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        self.function_dict = {'L': self.login, 'R': self.register, "E": self.do_exit, "F": self.find_words,
                              "H": self.history}

    # 接收客户端链接,生成进程
    def show(self):
        c, addr = self.server.accept()
        p = Process(target=self.handle, args=(c,))
        p.start()

    # 处理客户端函数
    def handle(self, c):
        cur = self.db.create_cursor()
        while True:
            data = c.recv(1024).decode()
            flog = data.split(' ')
            if flog[0] in self.function_dict:
                self.function_dict[flog[0]](c, flog[1], flog[2])
            else:
                pass

    def send_msg(self):
        pass

    # 登录方法
    def login(self, c, name, password):
        if self.db.login(name, password):
            c.send(b"OK")
        else:
            c.send(b"Fail")

    # 注册方法
    def register(self, c, name, password):
        if self.db.register(name, password):
            c.send(b"OK")
        else:
            c.send(b"Fail")

    # 退出方法
    def do_exit(self, c, name, password):
        c.send(b"OK")
        exit("客户端退出....")

    # 查询单词方法
    def find_words(self, c, name, word):
        r = self.db.find_words(name, word)
        if r:
            msg = r[0] + ":" + r[1]
            c.send(msg.encode())
        else:
            c.send("未查询到该单词".encode())

    # 查询历史记录方法
    def history(self, c, name, word):
        history_tuple = self.db.history(name)
        if history_tuple:
            for i in history_tuple:
                msg = str(i[0]) + " " + str(i[1]) + ":" + str(i[2]) + "\n"
                c.send(msg.encode())
        else:
            c.send("该用户没有历史记录....\n".encode())
        time.sleep(0.1)
        c.send(b"#")
