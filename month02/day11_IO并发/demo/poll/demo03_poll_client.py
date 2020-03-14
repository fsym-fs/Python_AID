"""
    test:
        从客户端可以循环的输入内容发送给服务端，每次发生都接收到服务端的回复
        从客户端输入“##” 两端程序都结束
"""
from socket import *

sockfd = socket()
server_addr = ("127.0.0.1", 8845)
sockfd.connect(server_addr)
while True:
    data = input(">>>:")
    if data == "##":
        sockfd.send(data.encode())
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server", data.decode())
sockfd.close()
