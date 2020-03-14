"""
    Theard03
        自定义线程类
"""
from threading import Thread
from time import sleep
import os,sys

class Mythread(Thread):
    def __init__(self):
        super().__init__()

    def fun01(self):
        sleep(4)
        print("fun01")

    def fun02(self):
        sleep(3)
        print("fun02")

    def run(self):
        self.fun01()
        self.fun02()


def fun03():
    sleep(6)
    print("fun03")


t = Mythread()
t.start()
fun03()
t.join()
# os.system("cat demo01_event.py>>tt.txt")

