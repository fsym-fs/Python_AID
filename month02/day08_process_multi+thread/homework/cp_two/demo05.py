"""
    自定义进程类
"""
from multiprocessing import Process
from typing import Optional, Callable, Any, Tuple, Mapping
from time import sleep


class TT(Process):
    def __init__(self):
        super().__init__()

    def f1(self):
        sleep(3)
        print("123")

    def f2(self):
        sleep(4)
        print("456")

    def run(self):
        self.f1()
        self.f2()


p = TT()
p.start()
p.join()
