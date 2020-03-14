"""

"""
from socket import *
import time
from month02.day07_process.homework.other.homework04 import *

socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
socket_server.bind(("192.168.1.6", 8444))
socket_server.listen(4)
def send_result():
    print("等待连接.....")
    c, addr = socket_server.accept()
    kind = c.recv(1024)
    c.send(b"OK")
    data = c.recv(1024)
    suffix = data.decode().split(".")[-1]
    with open("result." + suffix, "wb", 1) as f:
        while True:
            data = c.recv(1024)
            if not data:
                time.sleep(2)
                break
            f.write(data)
    result = baidu(kind.decode(),"result."+suffix)
    print(str(result))
    # c.send(str(result).encode())
    # print(result)
    # print(type(result))s
    print(str(result))

while True:
    send_result()
