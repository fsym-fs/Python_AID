"""
    实现对学生信息的增加、删除、修改和查询。
"""


class Students_model:
    def __init__(self, name=None, sex=None, age=None, grade=None, id=None, ):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = grade

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        if value == "男" or value == "女":
            self.__sex = value
        else:
            self.__sex = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            self.__age = None

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if value >= 0:
            self.__grade = value
        else:
            self.__grade = None


class Interface_views:
    def __init__(self):
        self.__students_controls = Students_controls()

    def __show_home_page(self):
        print("""
+-------------------------+
|   1)  添加学生信息        |
|   2)  显示学生信息        |
|   3)  删除学生信息        |
|   4)  修改学生成绩        |
|   5)  按学生成绩升序排序   |
|   6)  退出程序            |
+-------------------------+
        """)

    def __person_input(self):
        n = input("输入你想要进入的功能:")
        if n == "1":
            self.__input_students()
        elif n == "2":
            self.__output_all()
        elif n == "3":
            self.__show_del()
            self.__show_del_students()
        elif n == "4":
            pass
        elif n == "5":
            pass
        elif n == "6":
            print("正在退出程序,欢迎下次使用!   ^--^")
            return 6
        else:
            print("输入错误,请重新输入!")

    def __show_del(self):
        print("1)按学号删除")
        print("2)按姓名删除")
        print("3)按年龄删除")
        print("4)按性别删除")
        print("5)按成绩删除")
        print("6)返回上一层")

    def __show_del_students(self):
        while True:
            n = input("输入你要按什么删除:")
            if n == "1":
                m = input("请输入id:")
                self.__students_controls.del_students_id(m)
                break
            elif n == "2":
                m = input("请输入name:")
                self.__students_controls.del_students_name(m)
                break
            elif n == "3":
                m = input("请输入age:")
                self.__students_controls.del_students_age(m)
                break
            elif n == "4":
                m = input("请输入sex:")
                self.__students_controls.del_students_sex(m)
                break
            elif n == "5":
                m = input("请输入score:")
                self.__students_controls.del_students_score(m)
                break
            elif n == "6":
                break
            else:
                print("输入错误,请重新输入!")

    def __input_students(self):
        name = input("输入学生的姓名:")
        sex = input("输入学生的性别:")
        age = int(input("输入学生的年龄:"))
        grade = int(input("输入学生的成绩"))
        student = Students_model(name, sex, age, grade, id)
        self.__students_controls.add_students(student)

    def __output_all(self):
        self.__students_controls.show_students()

    def main(self):
        while True:
            self.__show_home_page()
            if self.__person_input() == 6:
                break


class Students_controls:
    def __init__(self):
        self.__list_students = []

    def show_students(self):
        for student in self.__list_students:
            print(student.id, student.name, student.sex, student.age, student.grade)

    def add_students(self, student):
        student.id = 1000 + len(self.__list_students)
        self.__list_students.append(student)

    def del_students_id(self, n):
        for i in range(len(self.__list_students) - 1, -1, -1):
            if self.__list_students[i].id == int(n):
                del self.__list_students[i]
                break

    def del_students_name(self, n):
        for i in range(len(self.__list_students) - 1, -1, -1):
            if self.__list_students[i].name == n:
                del self.__list_students[i]

    def del_students_age(self, n):
        for i in range(len(self.__list_students) - 1, -1, -1):
            if self.__list_students[i].age == int(n):
                del self.__list_students[i]

    def del_students_sex(self, n):
        for i in range(len(self.__list_students) - 1, -1, -1):
            if self.__list_students[i].sex == n:
                del self.__list_students[i]

    def del_students_score(self, n):
        for i in range(len(self.__list_students) - 1, -1, -1):
            if self.__list_students[i].score == int(n):
                del self.__list_students[i]


i = Interface_views()
i.main()
