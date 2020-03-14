import os
from time import sleep
"""
@所有人
各位同学,晚上7点钟有集团统一的授课,学员点击链接https://live.polyv.cn/watch/542640  验证码：254845,
大家准时上线参加,收到回复哈.
"""
pid = os.fork()
# print(pid)
if pid < 0:
    print("创建进程失败！")
elif pid == 0:
    sleep(3)
    print("新的进程")
else:
    sleep(4)
    print("原来的进程")
print("实验完毕")
