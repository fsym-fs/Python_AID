"""
僵尸进程演示
"""
import os, sys
import time
import signal
#忽略子进程的退出行为
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("子进程:", os.getpid())
    sys.exit("子进程退出")
else:
    print("父进程")
    # pid, status = os.wait()
    # print(pid,status)
    input()
