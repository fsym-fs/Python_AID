"""
    epoll
    只能用于Linux
    效率较高
    一开始就将关注的队列直接提交给操作系统并在操作系统中开辟空间，不需要映射。
    而在检测到就绪对象时，操作系统再告知应用层有具体就绪对象，不需要应用层自己遍历查找
"""
from socket import *
from select import *

# 创建TCP套接字
s = socket()
s.bind(("0.0.0.0", 8845))
s.listen(3)
s.setblocking(False)

# 关注IO
p = epoll()
p.register(s, EPOLLIN)

# 建立文件描述符地图,时刻与register保持一致
fdmap = {s.fileno(): s}
# 提交监控
while True:
    print("等待IO发生.....")
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            c.setblocking(False)
            print("From:", addr)
            # 将新的对象加入到关注队列（1,2,4,8、、）
            # p.register(c, EPOLLIN | EPOLLERR | EPOLLET)
            p.register(c, EPOLLIN | EPOLLET)
            # 更新文件描述符地图，时刻与register保持一致
            fdmap[c.fileno()] = c
        # 多个类型关注
        # elif event & EPOLLERR:
        #     pass
        else:
            data = fdmap[fd].recv(1024)
            print("data:", data.decode())
            if not data:
                p.unregister(fdmap[fd])
                fdmap[fd].close()
                del fdmap[fd]
                continue
            fdmap[fd].send(b"OK")
    # print(events)
