"""
Test06
    1.获取一个整数,如果是奇数则state="奇数",否则state="偶数"
    2.获取一个年份,如果是闰年,day=29,否则day=28
"""
# 1
number = "偶数" if int(input("输入一个整数:")) % 2 == 0 else "奇数"
print(str(number))
year = int(input("输入一个年份:"))
day = 29 if year % 400 == 0 or \
        year % 4 == 0 and \
        year % 100 != 0 else 28
print(str(day))

# 2
number = "偶数" if int(input("输入一个整数:")) % 2 else "奇数"
print(str(number))
year = int(input("输入一个年份:"))
day = 29 if not year % 400 \
            or not year % 4 \
            and year % 100 \
    else 28