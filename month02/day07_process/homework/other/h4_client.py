"""
客户端发送一个图片及图片的类别信息给服务端
"""
from socket import *

socket_client = socket(AF_INET, SOCK_STREAM)
server_addr = ("192.168.1.6", 8444)
socket_client.connect(server_addr)


def send_pic(pic_kind, pic_path):
    socket_client.send(pic_kind.encode())
    data = socket_client.recv(1024)
    if data.decode() == "OK":
        socket_client.send(pic_path.encode())
        with open(pic_path, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                socket_client.send(data)
        print("OK")
        # data = socket_client.recv(10)
        # print(data.decode())

send_pic("动物", "dog.jpg")
