from socket import *
import json


def test():
    s = socket()
    s.bind(("0.0.0.0", 8001))
    s.listen(3)
    c, addr = s.accept()
    data = c.recv(1024).decode()
    print(data)
    data = {'status': '200', 'data': 'ccccc'}
    c.send(json.dumps(data).encode())
    c.close()
    s.close()

test()