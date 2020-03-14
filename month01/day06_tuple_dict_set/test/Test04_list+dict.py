"""
Test04_dict
    循环录入学生的姓名,年龄,性别,成绩
    如果名称为空,停止录入
    打印最后一个/..的学生信息(一行一个)
    格式为:...的年龄是...,性别是...,成绩是...
    如果录入的是唐僧,则打印年龄
"""
print("录入学生的姓名,年龄,性别,成绩")
students = []
while True:
    name = input("姓名:")
    if name == "":
        break
    else:
        age = input("年龄:")
        sex = input("性别:")
        grade = input("成绩:")
        students.append({"name": name, "age": age, "sex": sex, "grade": grade})
for i in students:
    print("%s的年龄是%s,性别是%s,成绩是%s"%(i["name"],i["age"],i["sex"],i["grade"]))
print(students[-1])
