"""
Test11
   猜数字游戏:
    程序产生1-100之间的随机数
    在终端重复猜测,直到猜对为止
    提示:大了,小了,终于猜对了
"""
#1
import random
number = random.randint(1,100)
print("请输入你猜的数字")
n = int(input())
while n != number:
        if n <number :
            print("小了")
        else:
            print("大了")
        n = int(input())
else:
    print("终于猜对了")

#2
import random
number = random.randint(1,100)
while True:
    n = int(input("请输入你猜的数字"))
    if n <number :
        print("小了")
    elif n>number:
        print("大了")
    else:
        print("终于猜对了")
        break

