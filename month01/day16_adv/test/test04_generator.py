"""
    函数式编程:
        封装:分
        继承:隔
        多态:做

"""
"""
    定义函数,在老婆列表中,查找颜值大于90的所有老婆
    定义函数,在老婆列表中,查找存款小于10万的所有老婆
    步骤:
        根据需求创建函数
        运用函数思想:分,隔,做
"""

from common_model.iterable_tools import IterableHepler


class Wife:

    def __init__(self, name, face_score, money, age):
        self.name = name
        self.face_score = face_score
        self.money = money
        self.age = age

    def print_self(self):
        print("%s--%d--%d" % (self.name, self.face_score, self.money))


list_wifes = [
    Wife("双儿", 95, 5000, 25),
    Wife("苏荃", 98, 10000, 30),
    Wife("建宁", 86, 999999, 25),
    Wife("阿珂", 100, 6000, 23),
    Wife("铁锤", 60, 99, 35),
    Wife("曾柔", 100, 6000, 23),
]

# def find_face_score(item):
#     return item.face_score > 90
#
#
# def find_money(item):
#     return item.money < 100000
#
#
# for i in IterableHepler.find(list_wifes, find_face_score):
#     print(i.__dict__)
# print("-----------------------------------------------------------")
# for i in IterableHepler.find(list_wifes, find_money):
#     print(i.__dict__)
# # 返回老婆名字为"苏荃"的对象
# for i in IterableHepler.find_all(list_wifes, lambda item: item.name == "苏荃"):
#     print(i.__dict__)
# # 返回老婆颜值为100的对象,如有多个则返回第一个对象
# print((IterableHepler.find_single(list_wifes, lambda item: item.face_score == 100)).__dict__)
# # 在老婆列表中,查找所有老婆的姓名
# for i in IterableHepler.find(list_wifes,lambda item :(item.money,item.face_score)):
#     print(i)
# # 在老婆列表中,查找所有老婆的姓名和颜值
# for i in IterableHepler.find(list_wifes,lambda item:item.money):
#     print(i)
# print("---------------------------------------------------------------")
# for i in list_wifes:
#     print(i.name)
# for i in list_wifes:
#     print(i.name,i.face_score)
