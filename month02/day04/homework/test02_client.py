from socket import *

socket_client = socket()
client_addrs = ("192.168.1.6", 8765)
socket_client.connect(client_addrs)
data_path = input("请输入上传的头像路径:")
with open(data_path, "rb") as f:
    while True:
        file_byte = f.read(1024)
        socket_client.send(file_byte)
        if not file_byte:
            break
# data_result = socket_client.recv(1024)
# if data_result == b"OK":
print(data_path, "上传成功!")
socket_client.close()
