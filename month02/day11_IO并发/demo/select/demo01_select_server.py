"""
    select
        可用于 Windows,linux,Unix
        效率低，只能最多监控1024个
        每次都需要将关注的队列映射提交给操作系统，
        而在检测到就绪对象时，操作系统再告知应用层有就绪对象但需要应用层自己遍历查找

    通常情况下只会使用读对象，而不会使用写对象
    select 实现tcp服务
    【1】将关注的IO放入对应的监控类别列表
    【2】通过select函数进行监控
    【3】遍历select返回值列表，确定就绪IO事件
    【4】处理发生的IO事件
"""
from socket import *
from select import select

# 创建监听套接字
s = socket()
s.bind(("0.0.0.0", 8844))
s.listen(3)
# 将服务端设置为非阻塞
s.setblocking(False)

# 设置关注列表
rlist = [s]  # 处理客户端链接
wlist = []
xlist = []

while True:
    print("等待处理IO.......")
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历返回值列表，看看哪个IO就绪
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("From:", addr)
            # 将客户端设置为非阻塞
            c.setblocking(False)
            # 将对应的客户端链接套接字加入关注列表
            rlist.append(c)
        else:
            # 如果r遍历到客户端链接套接字说明: 有客户端给服务端发信息
            data = r.recv(1024)
            if not data:
                # 客户端退出
                rlist.remove(r)
                r.close()
                continue
            print("data:", data.decode())
            r.send(b"OK")
            """
                2.将主动发送信息的IO对象加入到写关注列表
                wlist.append(r)
            """

    for w in ws:
        """
           w.send(b"OK")
           wlist.remove(w) 
        """
        pass
    for x in xs:
        pass
