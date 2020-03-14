# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28
#"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(m"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28
"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         breakonth) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         breakr(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + """"
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break"月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         breakonth) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         breakr(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + """"
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break"月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(m"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28
"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         breakonth) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         breakr(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + """"
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28

# """
# Test07
#     循环执行,直到e
# """
# while True:
#     year = (input("输入一个年份:"))
#     month = int(input("输入一个月份:"))
#     year = int(year)
#     list01 = [1, 3, 5, 7, 8, 10, 12]
#     list02 = [2]
#     list03 = [4, 6, 9, 11]
#     if month in list01:
#         print(str(year)+"年"+str(month) + "月有31天")
#     elif month in list02:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             print(str(year)+"年"+str(month) + "月有29天")
#         else:
#             print(str(year)+"年"+str(month) + "月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break"月有28天")
#     elif month in list03:
#         print(str(year)+"年"+str(month) + "月有30天")
#     else:
#         print("您输入的月份不在(1-12)月当中!")
#     if input() == "e":
#         break
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有"""
# Test01
#     获取商品价格
#     获取购买数量
#     获取支付金额
#     支付 - 价格*数量
#     显示应该找回?元或者钱不够
# """
# # 获取支付金额
# pay = input("Input  pay:\n")
# # 获取商品价格
# price = input("Input price:\n")
# # 获取购买数量
# number = input("Input number:\n")
# # 显示应该找回?元
# change = int(pay) - int(price) * int(number)
# if change > 0:
#     print("Your change :   " + str(change) + " RMB")
# elif change == 0:
#     print("您的支付正好!")
# else:
#     print("钱不够")


# """
# Test02
#     获取季度(春夏秋冬)
#     显示相应的月份:
#     春天:1月-3月
#     夏天:4月-6月
#     秋天:7月-9月
#     冬天:10月-12月
# """
# """
#     1
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# elif quarter == "夏":
#     print("夏天:4月-6月")
# elif quarter == "秋":
#     print("秋天:7月-9月")
# else:
#     print("冬天:10月-12月")

# """
#     2
# """
# quarter = input("输入你要查询的季度\n")
# if quarter == "春":
#     print("春天:1月-3月")
# if quarter == "夏":
#     print("夏天:4月-6月")
# if quarter == "秋":
#     print("秋天:7月-9月")
# if quarter == "冬":
#     print("冬天:10月-12月")

# """
# Test03
#     录入4个同学的体重
#     打印最重的体重
#     算法:

# """

# """
#     1
# """
# Max_weight = 0
# print("输4名入同学的体重:")
# for i in range(0, 4, 1):
#     weight = int(input())
#     if weight > Max_weight:
#         Max_weight = weight
# print("Max_weight=" + str(Max_weight))

# """
#     2
# """
# Max_weight = 0
# weight_01 = int(input("输入同学的体重:"))
# weight_02 = int(input("输入同学的体重:"))
# weight_03 = int(input("输入同学的体重:"))
# weight_04 = int(input("输入同学的体重:"))
# if weight_01 > Max_weight:
#     Max_weight = weight_01
# if weight_02 > Max_weight:
#     Max_weight = weight_02
# if weight_03 > Max_weight:
#     Max_weight = weight_03
# if weight_04 > Max_weight:
#     Max_weight = weight_04
# print("Max_weight=" + str(Max_weight))

# """
#     3
# """
# Max_weight = 0
# weight_list = []
# weight = input("输4名入同学的体重:")
# weight_list = weight.split()
# print("Max_weight:" + str(max(weight_list)))

# """
# Test04
#     获取成绩
#     判断等级(优,良,及格,不及格,不在范围内(0-100))
# """
# results = int(input("输入成绩:"))
# if results >= 90 and results <= 100:
#     print("优秀")
# elif results >= 80:
#     print("良好")
# elif results >= 60:
#     print("及格")
# elif results < 60 and results >= 0:
#     print("不及格")
# else:
#     print("不在范围内(0-100)")

# """
# Test05
#     获取一个年份,一个月份
#     打印相应的天数
#     1 3 5 7 8 10 12 --> 31天
#     2 -->28(平年),29(闰年)
#     4 6 9 11 -->30
# """
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# list01 = [1, 3, 5, 7, 8, 10, 12]
# list02 = [2]
# list03 = [4, 6, 9, 11]
# if month in list01:
#     print(str(year)+"年"+str(month) + "月有31天")
# elif month in list02:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year)+"年"+str(month) + "月有29天")
#     else:
#         print(str(year)+"年"+str(month) + "月有28天")
# elif month in list03:
#     print(str(year)+"年"+str(month) + "月有30天")
# else:
#     print("您输入的月份不在(1-12)月当中!")

# """
# Test06
#     1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
#     2.获取一个年份,如果是闰年,day=29,否则day=28
# """
# # 1
# number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if year % 400 == 0 or \
#         year % 4 == 0 and \
#         year % 100 != 0 else 28
# print(str(day))

# # 2
# number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
# print(str(number))
# year = int(input("输入一个年份:"))
# day = 29 if not year % 400 \
#             or not year % 4 \
#             and year % 100 \
#     else 28









       