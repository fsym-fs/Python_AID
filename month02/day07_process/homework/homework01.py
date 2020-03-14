"""
1.  利用多进程完成文件的拆分

    有一个文件比较大，要拆分成两个，按照字节大小平均分
    一个进程去拷贝上半部分，与此同时另一个进程拷贝下本部分

    *  os.path.getsize()  seek()
"""
import os, sys
import signal

# 忽略子进程的退出行为
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    with open("dict01.txt", "r", 1) as f:
        n = os.path.getsize("dict01.txt")
        with open("dict02.txt", "w") as f1:
            while True:
                if f.tell() <= n // 2:
                    data = f.read(1024)
                    f1.write(data)
                else:
                    break
else:
    with open("dict01.txt", "r", 1) as f:
        n = os.path.getsize("dict01.txt")
        f.seek(n // 2, 0)
        with open("dict03.txt", "w") as f2:
            while True:
                data = f.read(1024)
                if data:
                    f2.write(data)
                else:
                    break
sys.exit("保存完成!")

