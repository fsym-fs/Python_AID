"""
    文件偏移量
        计时
            1.向一个文件中每隔2秒写入一行内容：
                1.  2020-01-01 12：12：12
                2.  2020-01-01 12：12：14
            2.打开文件随时可以看到已经写入的内容
            3.当程序终止后，重新启动后继续写并且行号可以衔接
"""
import time
with open("/home/tarena/month02/day03/test/1.txt","ab+") as f:
    n=1
    se = f.seek(0,0)
    for line in f:
        n+=1
    # se = f.seek(0,2)
    while True:
        loc = time.ctime()
        s = str(n)+"  "+loc+"\n"
        s = s.encode()
        f.write(s)
        f.flush()
        time.sleep(2)
        n+=1