from socket import *

socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind(("192.168.1.6", 8444))
socket_server.listen(3)
while True:
    c, addrs = socket_server.accept()
    print("from:", addrs)
    data = c.recv(2048)
    print(data.decode())
    # 发送http
    #     data = """HTTP/1.1 200 OK
    # Content-Type:text/html
    #
    # OK
    # """
    data = "HTTP/1.1 200 OK\r\n"
    data += "Content-Type:text/html\r\n"
    data += "\r\n"
    data += "Hello,World!"
    c.send(data.encode())
    c.close()
socket_server.close()
