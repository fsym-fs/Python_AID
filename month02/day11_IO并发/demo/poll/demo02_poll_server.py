"""
    poll
    可用于Linux,Unix
    效率低
    每次都需要将关注的队列映射提交给操作系统，
    而在检测到就绪对象时，操作系统再告知应用层有就绪对象但需要应用层自己遍历查找
"""
from socket import *
from select import *

# 创建TCP套接字
s = socket()
s.bind(("0.0.0.0", 8845))
s.listen(3)
s.setblocking(False)

# 关注IO
p = poll()
p.register(s, POLLIN)

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
            # p.register(c, POLLIN | POLLERR)
            p.register(c, POLLIN)
            # 更新文件描述符地图，时刻与register保持一致
            fdmap[c.fileno()] = c
        # 多个类型关注
        # elif event & POLLERR:
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
