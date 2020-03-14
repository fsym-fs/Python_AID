"""
Test04
    随机加法考试题
        程序产生2个随机数
        获取(a+b=?)两个数相加的结果
        答对加10分,否则减5分
        共3题,打印分数

"""
import random
import os
while True:
    result = 0
    for _ in range(3):
        number01 = random.randint(1,100)
        number02 = random.randint(1,100)
        s = int(input(str(number01)+"+"+str(number02)+"=?   "))
        result += 10 if s == number02+number01 else -5
        # if s == number02+number01:
        #     result +=10
        # elif s!=number02+number01:
        #     result-=5        
    if result<=0:
        print("您的分数为0分!")
    else:
        print("您的分数为"+str(result)+"分!")
    n = input("开始选择y,结束选择n:")
    i=os.system("clear")#linux清屏,cls   window清屏
    if n=="n":
        break
    
