"""
Test04
    list01 = [4,5,65,76,7,8]
    输入最大值(自己写算法)
"""
list01 = [4,5,65,76,7,8]
max_number=list01[0]
for i in range(1,len(list01),1):
    if list01[i] >max_number:
        max_number = list01[i]
print(max_number)