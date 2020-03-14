"""
    创建狗类
        数据:
            爱称,年龄,颜色,品种
        行为:
            吃,坐下
    创建两个狗对象,调用相应的作法,画出内存图
"""


class Dog:
    def __init__(self, name=None, age=None, color=None, kind=None):
        self.name = name
        self.age = age
        self.color = color
        self.kind = kind

    def eatting(self):
        print(self.name, "is eatting shit", sep=" ")

    def sitting(self):
        print(self.name, "is sitting", sep=" ")


def f(p1, p2):
    p1 = Dog("11", 3)
    p2.name = "22"
    p2.age = 55


first_dog = Dog("kk", 2, "黄色", "田园犬")
second_dog = Dog("kk", 2, "黄色", "田园犬")
f(first_dog, second_dog)
print(first_dog.age)
print(second_dog.age)
# a = first_dog
# a.name = "ll"
# a.age = 15
# print(a.name,a.age)
# print(first_dog.name,first_dog.age)
# first_dog.eatting()
# first_dog.sitting()
# second_dog = Dog("Ww", 1, "白色", "拉布拉多")
# second_dog.eatting()
# second_dog.sitting()
