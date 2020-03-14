"""
    继承:
        创建一个父类--动物类
                        吃
        一个子类--鸟
                    飞
        一个子类--狗
                    跑
"""


class Animals:
    def __init__(self,name):
        self.name = name
    def eatting(self):
        print("Eatting......")
class Birds(Animals):
    def __init__(self,name="",age=0):
        super().__init__(name)
        self.age = age
    def flying(self):
        print("Flying")
class Dogs(Animals):
    def running(self):
        print("Running")
# a = Animals()
b = Birds("jj")
print(b.name,b.age)
# d = Dogs()
# d.eatting()
# d.running()
# b.eatting()
# b.flying()
# print(isinstance(a,Animals))
# print(isinstance(b,Animals))
# print(isinstance(b,Birds))
# print(issubclass(Dogs,Animals))
# print(issubclass(Dogs,Birds))
# print(type(a) == type(b))
# print(type(a) == type(Animals))
# print(type(a))
# print(type(Animals))