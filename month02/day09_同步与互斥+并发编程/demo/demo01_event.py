"""
    event 线程同步与互斥
"""
from threading import Event, Thread

# 创建一个event对象
e = Event()
# e.wait()
# 在线程之间进行通信
s = None


def yzr():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    # 为主线程解除阻塞
    e.set()


t = Thread(target=yzr())
t.start()

# 主线程验证信息
print("说对口令就是自己人")
# 在主线程使用之前先阻塞
e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("对的")
else:
    print("死")

t.join()
