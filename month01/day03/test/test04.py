"""
Test04
    获取成绩
    判断等级(优,良,及格,不及格,不在范围内(0-100))
"""
results = int(input("输入成绩:"))
if results >= 90 and results <= 100:
    print("优秀")
elif results >= 80:
    print("良好")
elif results >= 60:
    print("及格")
elif results < 60 and results >= 0:
    print("不及格")
else:
    print("不在范围内(0-100)")