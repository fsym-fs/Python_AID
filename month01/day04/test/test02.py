"""
    获取一个任意整数   ---->123456
    输出每位相加的和 ----->1+2+3+4+5+6
"""
while True:
    try:
        number = input("输入一个任意整数:")
        result = 0
        for i in number:
                result +=int(i)
        print(result)
    except:
        break
