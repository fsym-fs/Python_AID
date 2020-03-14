"""
    @295245142407
    学生信息管理系统
    作业
        1. 三合一
        2. 当天练习独立完成（目标：两个类如何互相调用）
        3. 体会MVC执行流程(调试/内存图)
        4. 完成添加学生功能(实现Controller类中的add_student方法)
             -- 为学生设置id(自增长,从1000开始)
             -- 将学生追加到列表中作业
        1. 三合一
        2. 当天练习独立完成（目标：两个类如何互相调用）
        3. 体会MVC执行流程(调试/内存图)
        4. 完成添加学生功能(实现Controller类中的add_student方法)
             -- 为学生设置id(自增长,从1000开始)
             -- 将学生追加到列表中
"""


class StudentModel:
    """
        学生模型
    """

    def __init__(self, name="", age=0, sex="", score=0, id=0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score
        self.id = id


class StudentManagerView:
    """
        界面视图(逻辑)
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生信息")
        print("2)显示学生信息")
        print("3)删除学生信息")
        print("4)修改学生信息")
        print("5)按学生成绩升序排序")
        print("6)退出程序")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__show_del()
            self.__show_del_students()
        elif item == "4":
            self.__show_update()
            self.__update_students()
        elif item == "5":
            self.__sort_students()
        elif item == "6":
            print("正在退出程序,欢迎下次使用!   ^--^")
            return 0
        else:
            print("输入错误,请重新输入!")

    def main(self):
        while True:
            self.__display_menu()
            # self.__select_menu()
            if self.__select_menu() == 0:
                break

    def __input_students(self):
        name = input("请输入姓名：")
        sex = input("请输入性别：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name, age, sex, score)
        # ....
        self.__manager.add_student(stu)

    def __output_students(self):
        self.__manager.show_all()

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
                self.__manager.del_students_id(m)
                break
            elif n == "2":
                m = input("请输入name:")
                self.__manager.del_students_name(m)
                break
            elif n == "3":
                m = input("请输入age:")
                self.__manager.del_students_age(m)
                break
            elif n == "4":
                m = input("请输入sex:")
                self.__manager.del_students_sex(m)
                break
            elif n == "5":
                m = input("请输入score:")
                self.__manager.del_students_score(m)
                break
            elif n == "6":
                break
            else:
                print("输入错误,请重新输入!")

    def __show_update(self):
        print("1)修改成绩")
        print("2)修改年龄")
        print("3)返回上一层")

    def __update_students(self):
        while True:
            n = input("输入你要修改的选项:")
            if n == "1":
                m = input("请输入id:")
                l = input("输入成绩:")
                self.__manager.updata_score(m, l)
                break
            elif n == "2":
                m = input("请输入id:")
                l = input("输入年龄:")
                self.__manager.updata_age(m, l)
                break
            elif n == "3":
                break
            else:
                print("输入错误,请重新输入!")

    def __sort_students(self):
        self.__manager.sort_stu()
        self.__manager.show_all()


class StudentManagerController:
    """
        核心逻辑(控制)
    """
    id = 1000  # id初始值

    @classmethod
    def get_id(cls, stu):
        stu.id = cls.id
        cls.id += 1

    def __init__(self):
        self.__list_stu = []

    def show_all(self):
        print("学号", "姓名", "性别", "年龄", "成绩", sep=" ")
        # with open("st.txt", "r") as f:
        #     print(f.read())
        #     # print(type(f.read()))
        for student in self.__list_stu:
            print("学号", student.id, "姓名:", student.name, "性别:", student.sex, "年龄:", student.age, "成绩", student.score,
                  sep=" ")

    def add_student(self, stu_target):
        # 1. 为学生创建id
        # 2. 将学生加入到列表中__list_stu
        StudentManagerController.get_id(stu_target)
        # with open("st.txt", "a") as f:
        #     f.write(str(stu_target.id) + " ")
        #     f.write(str(stu_target.name) + " ")
        #     f.write(str(stu_target.sex) + " ")
        #     f.write(str(stu_target.age) + " ")
        #     f.write(str(stu_target.score))
        #     f.write("\n")
        self.__list_stu.append(stu_target)

    def del_students_id(self, n):
        """
        :param n:传入一个删除的id名
        :return:
        """
        for i in range(len(self.__list_stu) - 1, -1, -1):
            if self.__list_stu[i].id == int(n):
                del self.__list_stu[i]
                break

    def del_students_name(self, n):
        """

        :param n:传入一个删除的学生姓名
        :return:
        """
        for i in range(len(self.__list_stu) - 1, -1, -1):
            if self.__list_stu[i].name == n:
                del self.__list_stu[i]

    def del_students_age(self, n):
        """

        :param n:传入一个删除的学生的年龄
        :return:
        """
        for i in range(len(self.__list_stu) - 1, -1, -1):
            if self.__list_stu[i].age == int(n):
                del self.__list_stu[i]

    def del_students_sex(self, n):
        """

        :param n:传入一个删除的学生的性别
        :return:
        """
        for i in range(len(self.__list_stu) - 1, -1, -1):
            if self.__list_stu[i].sex == n:
                del self.__list_stu[i]

    def del_students_score(self, n):
        """

        :param n:传入一个删除的学生的分数
        :return:
        """
        for i in range(len(self.__list_stu) - 1, -1, -1):
            if self.__list_stu[i].score == int(n):
                del self.__list_stu[i]

    def updata_score(self, id, score):
        for student in self.__list_stu:
            if student.id == int(id):
                student.score = score
                break

    def updata_age(self, id, age):
        for student in self.__list_stu:
            if student.id == int(id):
                student.age = age
                break

    def sort_stu(self):
        for i in range(0, len(self.__list_stu) - 1):
            for j in range(i + 1, len(self.__list_stu)):
                if self.__list_stu[i].score > self.__list_stu[j].score:
                    self.__list_stu[i], self.__list_stu[j] = self.__list_stu[j], self.__list_stu[i]


view = StudentManagerView()
view.main()
