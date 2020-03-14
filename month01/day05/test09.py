"""
Test09
    将1970年到2050年之间的闰年存入列表
"""
#1
l1 = [i for i in range(1970,2051) if (i%4==0 and i%100!=0) or i%400==0]
print(l1)

#2
l2=[]
for i in range(1970,2051):
    if (i%4==0 and i%100!=0) or i%400==0:
        l2.append(i)
print(l2)
