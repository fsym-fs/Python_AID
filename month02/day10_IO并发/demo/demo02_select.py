"""
    IO多路复用示例-select
"""
from socket import socket
from select import select

f = open("test.log")

s = socket()
s.bind(("0.0.0.0", 8845))
s.listen(3)

print("IO监控")
rs, ws, xs = select([s], [], [], 10)
print("rlist", rs)
print("wlist", ws)
print("xlist", xs)
