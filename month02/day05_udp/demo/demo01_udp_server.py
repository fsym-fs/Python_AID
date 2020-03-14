"""
    UDP_server
"""
from socket import *

# 创建udp套接字
socket_server = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
socket_addr = ("192.168.1.6", 8844)
socket_server.bind(socket_addr)
# 循环收发信息
while True:
    data, addr = socket_server.recvfrom(1024)
    print("接收到%s的信息%s:" % (addr, data.decode()))
    socket_server.sendto(b"Thanks", addr)
# 关闭套接字
socket_server.close()
