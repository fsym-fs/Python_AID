import socket
# 创建套接字对象
sockefd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
sockefd.bind(("192.168.1.4", 8654))
# 192.168.1.4
# 设置监听套接字
sockefd.listen(3)
while True:
    # 处理客户端链接
    print("Writing....")
    connfd, addr = sockefd.accept()
    print("From", addr)
    # 收发信息(字节形式)
    while True:
        data = connfd.recv(1024)
        if data.decode()=="##":
            break
        print("Recv:", data.decode())
        n = connfd.send(b"Thanks")
        print("Send%d bytes" % n)
    # 关闭套接字
    connfd.close()
sockefd.close()
