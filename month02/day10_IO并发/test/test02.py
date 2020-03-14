import socket
import os
import time


class MySocket:
    ADDR = ("127.0.0.1", 23456)

    def __init__(self):
        self.__socketfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.__socketfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 连接服务端
        try:
            self.__socketfd.connect(self.ADDR)
        except:
            print("连接服务端出错!")

    @property
    def socketfd(self):
        return self.__socketfd


class ClientController:

    def __init__(self, c_socket, name="", file="", id=0):
        self.id = id
        self.name = name
        self.file = file
        self.socketfd = c_socket.socketfd

    def register(self, name, pwd):
        """
        用户注册请求
        Args:
            name: 用户名
            pwd: 密码
        Returns:注册结果:None 或者 (regist_status,msg)
        """
        data = "R " + name + " " + pwd
        self.socketfd.send(data.encode())
        data = self.socketfd.recv(1024)
        return ClientController.format_data_from_server(data)

    def login(self, name, pwd):
        """
        用户登录
        Args:
            name: 用户名
            pwd: 密码
        Returns:登录结果:None 或者(login_status,msg)
        """
        data = "L " + name + " " + pwd
        self.socketfd.send(data.encode())
        data = ClientController.format_data_from_server(self.socketfd.recv(1024))
        # 客户端信息更新 start
        if data and data[0]:
            self.name = name
            self.pwd = pwd
            self.id = data[1]
            self.file = "./" + self.name
            ClientController.make_dir(self.file)
            data[1] = "登录成功"
        # 客户端信息更新 end
        return data

    def quit(self):
        """
        退出登录
        Returns:None 或者 [True/False,msg]
        """
        self.socketfd.send(b"Q")
        data = ClientController.format_data_from_server(self.socketfd.recv(1024))
        if data and data[0]:
            self.socketfd.close()
        return data

    def find_file(self):
        """
        查看服务器上的文件
        Returns:None 或者[True/False,msg]
        """
        data = "F"
        self.socketfd.send(data.encode())
        data = self.socketfd.recv(1024)
        return ClientController.format_data_from_server(data)

    def download_file(self, file_name, show_progress):
        """
        从服务器下载指定文件
        Args:
            file_name: 服务器上待下载的文件名
            show_progress: 打印下载进度
        Returns:下载结果=>None 或者 [True/False,msg]
        """
        if not file_name:
            return [False, "文件名不能为空"]
        dir = self.file + "/" + file_name
        # 请求下载
        data = "D " + file_name
        self.socketfd.send(data.encode())
        # 允许下载
        data = ClientController.format_data_from_server(self.socketfd.recv(128))
        if data and data[0]:
            # 文件夹是否存在
            ClientController.make_dir(self.file)
            # 下载新文件
            with open(dir, "wb") as new_file:
                while True:
                    data = self.socketfd.recv(1024)
                    if not data:
                        return [False, "异常终止"]
                    elif data == b"FAIL":
                        return [False, "无该文件"]
                    elif data == b"FINISH":
                        show_progress([True, dir + ":下载完成"])
                        return [True, dir + ":下载完成"]
                    else:
                        new_file.write(data)
                        new_file.flush()
                        show_progress([True, dir + ":下载中..."])

    def upload_file(self, file, show_progress):
        """
        本地文件上传到服务器
        Args:
            file: 待上传的本地文件的路径
            show_progress: 打印上传进度
        Returns:上传结果=>None 或者 [True/False,msg]
        """
        if not file:
            return [False, "待上传文件的路径不能为空"]
        if not os.path.exists(file):
            return [False, file + ":不存在,无法上传!"]
        # 请求上传文件
        self.socketfd.send(b"U " + file.split("/")[-1].encode())
        data = ClientController.format_data_from_server(self.socketfd.recv(128))
        #连续发送消息,注意通过消息边界或者sleep处理粘包
        time.sleep(0.1)
        # 允许上传文件
        if data and data[0]:
            with open(file, "rb") as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        time.sleep(0.1)
                        self.socketfd.send(b"FINISH")
                        show_progress([True, file + ":上传完成"])
                        return [True, file + ":上传完成"]
                    else:
                        self.socketfd.send(data)
                        show_progress([True, file + ":上传中..."])

    @staticmethod
    def make_dir(name):
        if not name: return None
        dir = "./" + name
        if os.path.exists(dir): return None
        os.mkdir("./" + name)

    @staticmethod
    def format_data_from_server(data):
        """
        格式化服务器发来的数据
        Args:
            data: 服务器响应的数据
        Returns:若文件字节流则返回本身;若普通响应格式(xxx_status,msg),则返回(True/False,status)
        """
        if not data:
            return data
        try:
            result = data.decode()
        except:
            result = None
        else:
            result=result.split(" ",1)
        if result and result[0] in "OK FAIL":
            return [True if result[0] == "OK" else False, "" if len(result)<2 else result[1]]
        else:
            return data


class ClientView:
    def __init__(self):
        self.__init_view()

    def __init_view(self):
        self.my_socket = MySocket()
        self.client_mgr = ClientController(self.my_socket)

    def __register(self):
        """用户注册"""
        name = pwd = repwd = ""
        while not name:
            name = input("请输入帐号名:")
        while not pwd or not repwd or pwd != repwd:
            pwd = input("请输入帐号密码:")
            repwd = input("请再次输入帐号密码:")
            if pwd != pwd:
                print("两次密码不一致,请重新输入")
        data = self.client_mgr.register(name, pwd)
        if data:
            print(data[1])

    def __login(self):
        """用户登录"""
        name = pwd = ""
        while not name:
            name = input("请输入帐号名:")
        while not pwd:
            pwd = input("请输入帐号密码:")
        data = self.client_mgr.login(name, pwd)
        if data:
            print(data[1])
            if data[0]:
                self.__display_menu()

    def __quit(self):
        """退出"""
        data = self.client_mgr.quit()
        if data:
            print(data[-1])
            return data[0]

    def __find_file(self):
        """查看文件"""
        data = self.client_mgr.find_file()
        if data:
            print(data[1])

    def __download_file(self):
        """下载文件"""
        file_name = input("请输入需要下载的文件(例如:xxx.txt):   ")

        data = self.client_mgr.download_file(file_name, self.__show_progress)
        if data and not data[0]:
            print(data[1])

    def __upload_file(self):
        """用户登录"""
        file_name = input("请输入待上传文件的路径:")
        data = self.client_mgr.upload_file(file_name, self.__show_progress)
        if data and not data[0]:
            print(data[1])

    def __show_progress(self, data):
        """打印进度"""
        if data and data[0]:
            print(data[1])

    @staticmethod
    def input_number(tip):
        """
        工具:输入数字
        Args:
            tip:
        Returns:
        """
        while True:
            try:
                num = int(input(tip))
            except:
                continue
            return num

    def main(self):
        """登录/注册"""
        while True:
            print("1)注册")
            print("2)登录")
            print("3)关闭")
            index = ClientView.input_number("请输入选项数字:")
            if index == 1:
                self.__register()
            elif index == 2:
                self.__login()
            elif index == 3:
                break

    def __display_menu(self):
        while True:
            print("1)查看文件")
            print("2)下载文件")
            print("3)上传文件")
            print("4)退出登陆")
            index = ClientView.input_number("请输入选项数字:")
            if index == 1:
                self.__find_file()
            elif index == 2:
                self.__download_file()
            elif index == 3:
                self.__upload_file()
            elif index == 4:
                if self.__quit():
                    self.__init_view()
                    break


if __name__ == '__main__':
    ftp_client_view = ClientView()
    ftp_client_view.main()