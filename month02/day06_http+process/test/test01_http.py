"""
    搭建一个http服务,当浏览器发起请求的时候向浏览器发送网页
    将http处理部分封装成函数
    分析请求内容，如果请求是/则相应html
    如果请求内容是其他则响应404
"""
from socket import *


def analysis_html(file_path):
    with open(file_path, "r") as f:
        n = f.read()
    return n


def request(socket_server):
    c, addrs = socket_server.accept()
    print("from:", addrs)
    data = c.recv(2048)
    # 发送http
    #     data = """HTTP/1.1 200 OK
    # Content-Type:text/html
    #
    # OK
    # """
    h = data.decode().split(" ")
    if h[1] == "/":
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += analysis_html("hell.html")
    else:
        data = "HTTP/1.1 400 Not found\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += "Not html"
    c.send(data.encode())
    c.close()


def tcp_server():
    socket_server = socket(AF_INET, SOCK_STREAM)
    # 端口立即重用 (在bind之前)
    socket_server.bind(("192.168.1.6", 8444))
    socket_server.listen(3)
    while True:
        request(socket_server)
    socket_server.close()


tcp_server()
