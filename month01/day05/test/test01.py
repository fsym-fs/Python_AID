"""
Test01
    在终端终端循环输入学生成绩,如果为空,则停止
    打印最高分,最低分,平均分
"""
b = []
while True:
    a = input("输入学生的成绩:")
    if a == "":
        break
    else:
        b.append(a)
print("最高分为:%s,最低分为:%s,平均分为:%f" % (max(b),min(b),(sum(b)/len(b))))


