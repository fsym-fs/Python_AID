"""
Test08
    1.利用列表推导式生成1--50之间能被3或者5整除的数
    2.利用列表推导式生成5--60之间数字的平方
"""
# list02 = [1,2,3,5,6]
# list01 = [34,45,54]
# list02 = [item + 10 for item in list02 ]
# list02 = [item +10 for item in list01 if item % 2 ==0]

l1=[i for i in range(1,51) if i%3==0 or i%5==0]#生成1--50之间能被3或者5整除的数
print(l1)#输出列表
l2 = [i**2 for i in range(5,61) ]#生成5--60之间数字的平方
print(l2)#输出列表