"""
    1.在list01中找出所有字符串
    2.在list01当中找出偶数
"""
list01 = [10, "悟空", 80, 20, "八戒", 25]
# print(type(list01[1])==str)
for i in (item for item in list01 if type(item) == str):
    print(i)
for i in (item for item in list01 if type(item) == int if item % 2 == 0):
    print(i)
