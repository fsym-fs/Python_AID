from socket import *

socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind(("192.168.1.6", 8446))
socket_server.listen(3)
while True:
    c, addrs = socket_server.accept()
    print("from:", addrs)
    data = c.recv(2048)
    print(data.decode())
    c.close()
socket_server.close()
