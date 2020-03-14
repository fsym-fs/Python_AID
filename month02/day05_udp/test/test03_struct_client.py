"""
    从客户端输入一个学生的信息：
        id name age score
    将信息打包发送给服务端
    服务端收到信息之后如果成绩大于90，则讲信息写入文件中，每个程序写一行
"""
from socket import *
import struct

socket_client = socket(AF_INET, SOCK_DGRAM)
server_addr = ("192.168.1.6", 8568)
while True:
    str_stu = input("输入一个学生的信息:")
    if not str_stu:
        break
    stu = str_stu.split(" ")
    id = int(stu[0])
    name = stu[1]
    age = int(stu[2])
    score = float(stu[3])
    n = len(name)
    st = struct.Struct("i" + str(n) + "sif")
    data = st.pack(id, name.encode(), age, score)
    socket_client.sendto(str(n).encode(), server_addr)
    socket_client.sendto(data, server_addr)
    print("发送成功!")
socket_client.close()
