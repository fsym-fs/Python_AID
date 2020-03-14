"""
Test02
    在终端循环输入学生姓名,如果录入为空,则停止,倒序输出所有人
    要求:姓名不能重复,如果重复提示,不存储
"""
b = []
while True:
    a = input("输入学生的姓名:")
    if a == "":
        break
    else:
        if a not in b:
            b.append(a)
        else:
            continue
for i in range(len(b)-1, -1, -1):
    print(b[i])