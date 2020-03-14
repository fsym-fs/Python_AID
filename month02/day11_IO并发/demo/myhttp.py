"""
搭建一个http服务，当浏览器发起请求的时候向浏览器发送 index.html 网页

* 将http处理部分封装为函数
* 分析请求内容，如果请求内容是 / 则响应 index.html网页
  如果请求内容是其他的则响应404

思路：参考http_test,将响应体改为index.html内容即可
     如果分析响应内容则使用split函数切割获取响应内容，看看是不是/
升级:
    使用IO多路复用方法形成IO的并发操作处理
    使用类进行封装
    网页有多个页面

重点代码
"""

from socket import *
from select import *


class HTTP_two:
    def __init__(self, HOST="0.0.0.0", POST=8888, DIR=None):
        self.HOST = HOST
        self.POST = POST
        self.DIR = DIR
        self.s = socket()
        self.s.bind((self.HOST, self.POST))
        self.s.listen(3)
        self.s.setblocking(False)
        self.ep = epoll()
        self.ep.register(self.s, EPOLLIN)
        self.epoll_dict = {self.s.fileno(): self.s}

    # 服务端功能
    def use(self):
        while True:
            print("等待链接.....")
            events = self.ep.poll()
            for fd, event in events:
                if fd == self.s.fileno():
                    self.server_handle(self.epoll_dict[fd])
                else:
                    flog = self.client_handle(self.epoll_dict[fd])

    # 服务端接收客户端链接
    def server_handle(self, fd):
        c, addr = fd.accept()
        c.setblocking(False)
        print("From:", addr)
        # 添加监控
        self.ep.register(c, EPOLLIN | EPOLLET)
        # 更新监控对象对应字典
        self.epoll_dict[c.fileno()] = c

    # 客户端请求处理
    def client_handle(self, fd):
        data = fd.recv(2048)
        print("data:", data.decode())
        if not data:
            self.http_response_exit(fd, "")
            return -1
        info = data.decode().split(' ')[1]
        print("请求内容：", info)
        if info[0] == '/':
            # 将网页给客户端
            data = self.http_response_home(fd, info)
        else:
            data = self.http_response_error(fd, info)

        fd.send(data.encode())  # 发送响应内容

    # 客户端http请求退出
    def http_response_exit(self, fd, info):
        self.ep.unregister(fd)
        fd.close()
        del fd

    # 客户端http请求访问
    def http_response_home(self, fd, info):
        # 将网页给客户端
        f = None
        if info == "/":
            f = open('/index.html')
        try:
            f = open("static" + info)
        except:
            data = self.http_response_error(fd, info)
            return data
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += f.read()
        f.close()
        return data

    # 客户端http请求访问错误
    def http_response_error(self, fd, info):
        data = "HTTP/1.1 404 Not Found\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += "Sorry...."
        return data


if __name__ == '__main__':
    """
        希望通过使用这个类,可以快速搭建一个服务,展示我的网页
    """
    # 用户自己决定的内容
    HOST = "0.0.0.0"
    POST = 8844
    DIR = "./static"
    my = HTTP_two(HOST, POST, DIR)
    my.use()
