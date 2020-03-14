"""
    udp_client
"""
from socket import *

# 创建套接字
socket_client = socket(AF_INET, SOCK_DGRAM)
# 服务端地址
server_addr = ("192.168.1.6", 8844)
# 发送信息
while True:
    data = input(">>>:")
    if not data:
        break
    socket_client.sendto(data.encode(), server_addr)
    data, addr = socket_client.recvfrom(1024)
    print("服务端:", data.decode())
socket_client.close()
