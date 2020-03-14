"""
Test03_list+dict
    循环录入学生的姓名,年龄,性别,成绩
    如果名称为空,停止录入
    打印所有学生信息(一行一个)
    格式为:...的年龄是...,性别是...,成绩是...
    如果录入的是唐僧,则打印年龄
"""
print("录入学生的姓名,年龄,性别,成绩")
students = {}
while True:
    name = input("姓名:")
    if name == "":
        break
    else:
        age = input("年龄:")
        sex = input("性别:")
        grade = input("成绩:")
        students[name] = [age,sex,grade]
for key, value in students.items():
    print("%s的年龄是%s,性别%s,成绩%s" % (key,value[0],value[1],value[2]))
try:
    print(students["唐僧"][2])
except:
    pass
