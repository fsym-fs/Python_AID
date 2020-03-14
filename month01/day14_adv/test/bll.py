"""
    bll.py ---->xxxControls
"""
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
        for student in self.__list_stu:
            print("学号", student.id, "姓名:", student.name, "性别:", student.sex, "年龄:", student.age, "成绩", student.score,
                  sep=" ")

    def add_student(self, stu_target):
        StudentManagerController.get_id(stu_target)
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