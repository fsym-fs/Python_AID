from socket import *

socket_client = socket(AF_INET, SOCK_DGRAM)
server_addr = ("192.168.1.6", 8855)
while True:
    data = input("输入单词:")
    socket_client.sendto(data.encode(), server_addr)
    result, addr = socket_client.recvfrom(1024)
    print(result.decode())
    if not data:
        break
socket_client.close()
