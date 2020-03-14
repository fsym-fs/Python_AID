"""
Test07
    循环执行,直到e
"""
while True:
    year = (input("输入一个年份:"))
    month = int(input("输入一个月份:"))
    year = int(year)
    list01 = [1, 3, 5, 7, 8, 10, 12]
    list02 = [2]
    list03 = [4, 6, 9, 11]
    if month in list01:
        print(str(year)+"年"+str(month) + "月有31天")
    elif month in list02:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(str(year)+"年"+str(month) + "月有29天")
        else:
            print(str(year)+"年"+str(month) + "月有28天")
    elif month in list03:
        print(str(year)+"年"+str(month) + "月有30天")
    else:
        print("您输入的月份不在(1-12)月当中!")
    if input() == "e":
        break