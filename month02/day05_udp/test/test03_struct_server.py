"""
    从客户端输入一个学生的信息：
        id name age score
    将信息打包发送给服务端
    服务端收到信息之后如果成绩大于90，则讲信息写入文件中，每个程序写一行
"""
from socket import *
import struct

# socket.AF_INET,socket.SOCK_STREAM
socket_server = socket(AF_INET, SOCK_DGRAM)
socket_server.bind(("192.168.1.6", 8568))
while True:
    print("等待链接.........")
    data_n, addrs1 = socket_server.recvfrom(1024)
    n = data_n.decode()
    data, addrs = socket_server.recvfrom(1024)
    if addrs == addrs1:
        print("来自:", addrs)
        data = struct.unpack("i" + str(n) + "sif", data)
        data[1].decode().strip("\x00")
        f = open("stu.txt", "a", 1)
        if data[-1] > 90:
            f.write(str(data) + "\n")
        print("接收成功!")
        f.close()
socket_server.close()
