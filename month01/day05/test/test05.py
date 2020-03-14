"""
Test05
    斐波那契数列:
        1,1,2,3,5,8,13...
        f(n+2)=f(n+1)+f(n),n>=3
    在终端中获取斐波那契数列的长度,打印列表
"""

#1
while True:
    try:
        s = input("输入斐波那契数列的长度:")
        if s == "":
            print("退出程序!")
            break
        else:
            list01 = []
            for i in range(0,int(s),1):
                if i ==0 or i==1:
                    list01.append(1)
                else:
                    list01.append(list01[i-1]+list01[i-2])
            print(list01)
    except :
        break

#2
fei_list = [1, 1]
length = int(input("请输入斐波那契数列的长度："))
i = 2
while i < length:
    if i >= 2:
        fei_list.append(fei_list[i - 1] + fei_list[i - 2])
        i += 1
print(fei_list)

#3
fei_list = [1, 1]
length = int(input("请输入斐波那契数列的长度："))
i = 2
for _ in range(length-2):
    fei_list.append(fei_list[-1]+fei_list[-2])
print(fei_list)

