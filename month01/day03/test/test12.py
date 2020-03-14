"""
    1.三合一(代码+图片+文档)
    2.当前练习独立完成
    3.在终端当中获取月份,显示季度
    4.bmi=体重(kg)/h的平方(m)
        小于18.5(不包含)  -->  体重过清
        18.5 --24(不包含)  -->  体重正常
        24--28(不包含)  -->  超重
        28 --30(不包含)  -->  I度肥胖
        30 --40(不包含)  -->  II度肥胖
        40---   --->III度肥胖
    5.在终端中录入年龄
        显示:如果录入空字符串,则停止录入
            0-1-->婴儿
            2-13-->儿童
            14-20-->青少年
            21-65 --->成年人
            66-  --->老年人
"""

#在终端当中获取月份,显示季度
list01 = [1,2,3]
list02=[4,5,6]
list03=[7,8,9]
list04=[10,11,12]
while True:
    try:
        month = int(input("输入月份:"))
        if month in list01:
            print("春天")
        elif month in list02:
            print("夏天")
        elif month in list03:
            print("秋天")
        elif month in list04:
            print("冬天")
        else:
            print("输入错误(1-12)!")
    except :
        break
# if month in list01:
#     print("春天")
# elif month in list02:
#     print("夏天")
# elif month in list03:
#     print("秋天")
# elif month in list04:
#     print("冬天")
# else:
#     print("输入错误(1-12)!")

#           bmi=体重(kg)/h的平方(m)
#         小于18.5(不包含)  -->  体重过清
#         18.5 --24(不包含)  -->  体重正常
#         24--28(不包含)  -->  超重
#         28 --30(不包含)  -->  I度肥胖
#         30 --40(不包含)  -->  II度肥胖
#           40---   --->III度肥胖
w = float(input("输入体重(kg):"))
h = float(input("输入身高(m):"))
s = w/h/h
if s < 18.5:
    print("体重过清")
elif s<24:
    print("体重正常")
elif s <28:
    print("超重")
elif s <30:
    print("I度肥胖")
elif s <40:
    print("II度肥胖")
else:
    print("III度肥胖")

# 5.在终端中录入年龄
# 显示:如果录入空字符串,则停止录入
# 0-1-->婴儿
# 2-13-->儿童
# 14-20-->青少年
# 21-65 --->成年人
# 66-  --->老年人
while True:
    flog = input("输入年龄:")
    age = int(flog)
    if age == None:
        break
    elif 0<=age <=1:
        print("婴儿")
    elif age <=13:
        print("儿童")
    elif age <=20:
        print("青少年")
    elif age <=65:
        print("成年人")
    else:
        print("老年人")
    if input()=="":
        break
