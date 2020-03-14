"""
    test01:udp
        客户端可以循环输入单词，获取单词解释
"""
"""
        使用dict文件，完成单词的查找
        1.使用input 输入一个单词
        2.查找到这个单词，打印出该单词，及其解释
        3.每个单词占一行，单词与解释之间有空格
    """

from socket import *


def file_line_all(n):
    # n = input("输入一个单词:")
    for line in open("dict.txt", "r"):
        a = line.split(" ")
        if a[0] > n:
            return "查无此单词！"
        elif n == a[0]:
            return line
    return "查无此单词！"


socket_server = socket(AF_INET, SOCK_DGRAM)
server_addr = ("192.168.1.6", 8855)
socket_server.bind(server_addr)
print("等待传输.....")
while True:
    data, addr = socket_server.recvfrom(1024)
    print("接收到",addr)
    result = file_line_all(data.decode())
    socket_server.sendto(result.encode(), addr)
socket_server.close()
