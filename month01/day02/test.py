# """
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元
# """
# #获取支付金额
# pay = input("Input  pay:\n")
# #获取商品价格
# price = input("Input price:\n")
# #获取购买数量
# number = input("Input number:\n")
# #显示应该找回?元
# change  = int(pay) - int(price)* int (number)
# print("Your change :   "+  str(change)+" RMB")

# """
# Test02
#     获取一个min
#     获取一个hour
#     获取day
#     显示:?day?hour?min共?s
# """
# #获取一个min
# minu = input("Input Minu:\n")
# #获取一个hour
# hour = input("Input Hour:\n")
# #获取day
# day = input("Input Day:\n")
# #共?s
# s1 = int(day)*24*60*60
# s2 = int(hour)*60*60
# s3 = int(minu)*60
# s = s1+s2+s3
# print(day+"-"+hour+"-"+minu+"=="+str(s)+"s")

# """
# Test03
#     古代称:一斤十六两
#     获取两,显示几斤零几两
# """
# liang = input("Input liang:\n")
# jin = int(liang)//16
# lian = int(liang)%16
# print(str(jin)+"斤"+str(lian)+"两")

# """
# Test04
#     公式:
#         距离=初速度*时间/2+加速度*时间的平方
#     已知:
#         距离,时间,初速度
#     计算:
#         加速度并打印
# """
# #输入距离
# distance = input("Input  distance:\n")
# #输入初速度
# initial_velocity = input("Input Initial velocity:\n")
# #输入时间
# time = input("Input time:\n")
# #公式   距离=初速度*时间/2+加速度*时间的平方
# acceleration =(int(distance)- int(initial_velocity)*(int(time)/2))/(int(time)**2)
# #输出加速度
# print("acceleration="+str(acceleration))

# """
# Test04
#     获取一个四位整数1234
#     输出每位相加的和
# """
# """
#     1
# """
# number = input("请输入一个四位整数:\n")
# number = int(number)
# bits = number%10
# ten = number//10%10
# thousand = number//100%10
# ten_thousand_bit = number//1000
# print(int(bits)+ten+thousand+ten_thousand_bit)

# """
#     2
# """
# number = input("请输入一个四位整数:\n")
# number = int(number)
# result = number%10
# result  + = number//10%10
# result  += number//100%10
# result  + = number//1000
# print(result)

# """
#     3
# """
# number = input("请输入一个四位整数:\n")
# number = int(number)
# result = 0
# for i in range(0,4,1):
#     result += number%10
#     number = number//10
# print(result)

"""
Test05
    获取一个年份
    是闰年输入True
    不是则为false
    条件:
        1.被4整除但不能被100整除
        2.能被400整除
"""
"""
    获取一个年份
"""
year    =   int(input("输入一个年份:\n"))
"""
    条件:
            1.被4整除但不能被100整除
            2.能被400整除
    是闰年输入True
    不是则为false
"""
if (year%4==0 and year%100!=0) or year%400==0:
    print("True")
else:
    print("false")