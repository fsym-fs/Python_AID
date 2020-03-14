"""
作业
1. 三合一
2. 当前练习独立完成
3. 在终端中获取一个矩形边长,打印矩形。
   例如：4
   ****
   *    *
   *    *
   ****
   例如：6
   ******
   *        *
   *        *
   *        *
   *        *
   ******
4. 在终端中判断一个字符串是否是回文
    例如：上海自来水来自海上
5. （扩展）一个小球从100米高度落下,每次弹回原高度一半(最小弹起高度0.01m)
   请计算：
   -- 总共弹起多少次？
   -- 整个过程走了多少米？
6. 看教程
   www.runoob.com
7. 阅读
    程序员的数学第四章,数学归纳法.

0.006062000000000012
0.00914100000000001

"""
# 3
"""
    1
"""
import time
l = int(input("输入一个矩形边长:"))
start = time.clock()
for i in range(0, l, 1):
    if i == 0 or i == l-1:
        print("*"*l)
    else:
        print("*"+" "*(l-2)+"*")
end = time.clock()
print("final is in ", end-start)
"""
    2
"""
l = int(input("输入一个矩形边长:"))
start = time.clock()
for i in range(0, l, 1):
    for j in range(0, l, 1):
        if i == 0 or i == l-1:
            print("*", end="")
        else:
            if j == 0 or j == l-1:
                # print(j)
                print("*", end="")
            else:
                print(" ", end="")
    print("")
end = time.clock()
print("final is in ", end-start)

# 4
str_word = input("输入一个字符串:")
t = 0
for i in range(0, len(str_word)//2+1, 1):
    if str_word[len(str_word)-1-i] != str_word[i]:
        t = 0
        break
    else:
        t = 1
if t == 1:
    print("是回文")
else:
    print("不是回文")

# 5
l = 100
i = 0
s = l
while l /2>= 1e-2:
    l = l/2
    i += 1
    s += l*2
print("整个过程走了%.2f米" % s)
print("总共弹起%d次" % i)
