"""
    usl.py ---->xxxViews
"""
from month01.day14_adv.test.bll import StudentManagerController
from month01.day14_adv.test.model import StudentModel


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

    def __trans(self, n):
        while True:
            try:
                return int(n)
            except ValueError:
                print("输入错误,请重新输入...")
                n = input("请重新输入一个数值!:")

    def __input_students(self):
        name = input("请输入姓名：")
        sex = input("请输入性别：")
        age = self.__trans(input("请输入年龄："))
        score = self.__trans(input("请输入成绩："))
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
                m = self.__trans(m)
                self.__manager.del_students_id(m)
                break
            elif n == "2":
                m = input("请输入name:")
                self.__manager.del_students_name(m)
                break
            elif n == "3":
                m = input("请输入age:")
                m = self.__trans(m)
                self.__manager.del_students_age(m)
                break
            elif n == "4":
                m = input("请输入sex:")
                self.__manager.del_students_sex(m)
                break
            elif n == "5":
                m = input("请输入score:")
                m = self.__trans(m)
                self.__manager.del_students_score(m)
                break
            elif n == "6":
                break
            else:
                print("输入错误,请重新输入")

    def __show_update(self):
        print("1)修改成绩")
        print("2)修改年龄")
        print("3)返回上一层")

    def __update_students(self):
        while True:
            n = input("输入你要修改的选项:")
            if n == "1":
                m = input("请输入id:")
                m = self.__trans(m)
                l = input("输入成绩:")
                l = self.__trans(l)
                self.__manager.updata_score(m, l)
                break
            elif n == "2":
                m = input("请输入id:")
                m = self.__trans(m)
                l = input("输入年龄:")
                l = self.__trans(l)
                self.__manager.updata_age(m, l)
                break
            elif n == "3":
                break
            else:
                print("输入错误,请重新输入!")

    def __sort_students(self):
        self.__manager.sort_stu()
        self.__manager.show_all()
