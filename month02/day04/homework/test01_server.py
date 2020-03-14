"""
练习1： 
        从客户端可以循环的输入内容发送给服务端，每次发送都接收到服务端回复Thranks。
        从客户端输入 ‘##’ 两端程序都结束
作业： 上传头像  将一个图片从给客户端发送给服务端
      思路：  客户端  读取头像图片内容--》通过网络发送给服务端
             服务端  从网路中接收内容--》写入到服务端的文件
      * 网络函数和流程，熟悉
"""
from socket import *

# socket.AF_INET,socket.SOCK_STREAM
socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind(("192.168.1.6", 8765))
socket_server.listen(5)
while True:
    print("等待链接.........")
    connfd, addrs = socket_server.accept()
    print("来自:", addrs)
    with open("pic02.png", "wb") as f:
        while True:
            data_file = connfd.recv(1024)
            # print(data_file)
            if not data_file:
                break
            f.write(data_file)
    print("接收成功!")
    connfd.close()
socket_server.close()
