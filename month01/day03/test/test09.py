"""
Test09
    获取一个开始值,再获取一个结束值
    打印中间值
    5--10    6789
    10--5    9876
"""
while True:
    i = int(input("输入一个开始值:"))
    j = int(input("输入一个开始值:"))
    if i>j:
        i,j=j,i
    while i<j-1:
        i+=1
        print(i)
    if input()=="n":
        break


# if i<=j:
#     while i<j:
#         i+=1
#         print(i)
# else:
#     while j<i:
#         j+=1
#         print(j)