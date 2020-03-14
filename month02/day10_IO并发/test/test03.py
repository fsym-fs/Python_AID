import socket
import os
import signal
import time
from threading import Thread
from multiprocessing import Lock

# 自动处理子进程退出状态
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


class MySocket:
    """
    服务端socket基于TCP
    """
    ADDR = ("0.0.0.0", 23456)

    def __init__(self):
        self.__socketfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.__socketfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        self.__socketfd.bind(self.ADDR)
        self.__socketfd.listen(3)

    @property
    def socketfd(self):
        return self.__socketfd


class Client:
    """
    客户端类
    """

    def __init__(self, id=0, name="", pwd="", file=""):
        self.id = id
        self.name = name
        self.pwd = pwd
        self.file = file


class ClientController:
    """
    客户端类控制器
    """
    FTP_DIR = "./ftp"

    def __init__(self):
        # 创建FTP根目录
        ClientController.make_dir(self.FTP_DIR)
        # 启用同步互斥锁解决并发问题
        self.__lock = Lock()
        # 已注册的账号列表
        self.__list_client = []

    def regist(self, connfd, name, pwd):
        """
        客户端注册账号
        Args:
            connfd: 客户端连接套接字
            name: 账号
            pwd: 密码
        """
        with self.__lock:
            if not name:
                return ClientController.response(connfd, "FAIL 用户名不能为空")
            if not pwd:
                return ClientController.response(connfd, "FAIL 密码不能为空")
            user = self.__find_by_name(name)
            if user:
                return ClientController.response(connfd, "FAIL 用户已存在")

            # 注册用户信息 -> 新增到用户列表
            client = Client()
            client.id = int(time.time())
            client.name = name
            client.pwd = pwd
            client.file = ClientController.FTP_DIR + "/" + name
            # 存入客户端列表
            self.__add_user(client)
            ClientController.make_dir(client.file)
            return ClientController.response(connfd, "OK 注册成功")

    def login(self, connfd, name, pwd):
        """
        客户端登录账号
        Args:
            connfd: 客户端连接套接字
            name: 账号
            pwd: 密码
        return 返回客户端对象
        """
        if not name:
            return ClientController.response(connfd, "FAIL 用户名不能为空")
        if not pwd:
            return ClientController.response(connfd, "FAIL 密码不能为空")
        user = self.__find_by_name(name)
        if not user:
            return ClientController.response(connfd, "FAIL 用户不存在")
        if user.pwd != pwd:
            return ClientController.response(connfd, "FAIL 密码错误")
        ClientController.make_dir(ClientController.FTP_DIR + "/" + name)
        ClientController.response(connfd, "OK " + str(user.id))
        return user

    def quit(self, connfd):
        """
        客户端退出登录
        Args:
            connfd:  客户端连接套接字
        """
        ClientController.response(connfd, "OK 帐号已退出")
        connfd.close()

    def find_file(self, connfd, dir):
        """
        客户端查看自己目录下的文件列表
        Args:
            connfd: 客户端连接套接字
            dir: 用户目录
        """
        ClientController.make_dir(dir)
        list_file = os.listdir(dir)
        list_file = " ".join(list_file)
        return ClientController.response(connfd, "OK " + list_file)

    def download_file(self, connfd, file_path):
        """
        客户端请求下载文件
        Args:
            connfd: 客户端连接套接字
            file_path: 文件路径
        """
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                ClientController.response(connfd, "OK 允许下载")
                #连续发送消息,注意通过消息边界或者sleep处理粘包
                time.sleep(0.1)
                while True:
                    data = f.read(1024)
                    if not data:
                        time.sleep(0.1)
                        return ClientController.response(connfd, b"FINISH")
                    else:
                        ClientController.response(connfd, data)
        else:
            ClientController.response(connfd, b"FAIL")

    def upload_file(self, connfd, file_path):
        """
        客户端上传文件
        Args:
            connfd: 客户端连接套接字
            file_path: 存放于服务器上该文件的路径
        """
        with open(file_path, "wb") as f:
            ClientController.response(connfd, "OK 允许上传")
            while True:
                data = connfd.recv(1024)
                if not data or data == b"FINISH":
                    break
                else:
                    f.write(data)
                    f.flush()

    def handle_illegal(self, connfd):
        """
        处理无法识别的请求
        Args:
            connfd: 客户端连接套接字
        """
        ClientController.response(connfd, "FAIL 非法请求")

    def __find_by_name(self, name):
        """
        根据名字在客户端列表中查询用户
        Args:
            name: 名字
        Returns:客户端对象
        """
        for user in self.__list_client:
            if user.name == name:
                return user

    def __add_user(self, client):
        """
        将客户端对象存入用户列表
        Args:
            client: 客户端对象
        """
        self.__list_client.append(client)

    @staticmethod
    def make_dir(dir):
        """
        创建文件夹(目录)
        Args:
            dir: 文件夹(目录)路径
        """
        if not dir: return None
        if os.path.exists(dir): return None
        os.mkdir(dir)

    @staticmethod
    def response(connfd, respone_str):
        """
        响应客户端请求
        Args:
            respone_str: 响应内容
        Returns:
        """
        if type(respone_str) != bytes:
            respone_str = respone_str.encode()
        connfd.send(respone_str)


class ServerController:
    def __init__(self):
        # 创建socket对象
        self.__my_socket = MySocket()
        # 创建客户端管理对象
        self.__client_mgr = ClientController()

    def main(self):
        while True:
            # 客户端连接套接字
            print("waiting for connect...")
            connfd, addr = self.__my_socket.socketfd.accept()
            print(addr, ":已连接")
            thread = Thread(target=self.__handle, args=(connfd,))
            thread.daemon = True
            thread.start()

    def __handle(self, connfd):
        """
        [线程]客户端收发消息
        Args:
            connfd:客户端连接套接字
        """
        client = None
        while True:
            data = connfd.recv(1024)
            data = data.decode()
            if not data or data.strip() == "Q":
                # 客户端断开连接 or 退出登录
                self.__client_mgr.quit(connfd)
                break
            data = data.split(" ", 1)
            if data[0] == "R":
                # 注册帐号
                name, pwd = data[1].split(" ", 1)
                self.__client_mgr.regist(connfd, name, pwd)
            elif data[0] == "L":
                # 登录帐号
                name, pwd = data[1].split(" ", 1)
                client = self.__client_mgr.login(connfd, name, pwd)
            elif data[0] == "F":
                # 查看文件
                self.__client_mgr.find_file(connfd, client.file)
            elif data[0] == "D":
                # 下载文件
                self.__client_mgr.download_file(connfd, client.file + "/" + data[1])
            elif data[0] == "U":
                # 上传文件
                print(client.file + "/" + data[1])
                self.__client_mgr.upload_file(connfd, client.file + "/" + data[1])
            else:
                self.__client_mgr.handle_illegal(connfd)


if __name__ == '__main__':
    server_mgr = ServerController()
    server_mgr.main()