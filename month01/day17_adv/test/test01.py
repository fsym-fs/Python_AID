"""
    函数式编程
        封装:封
        继承:隔
        多态:做
    lambda xx : xxx
    高阶函数:将函数作为参数或者返回值的函数
        map()
        filter()
        max()
        min()
        sorted()
"""


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
    Wife("沐剑屏", 86, 6000, 24),
    Wife("阿珂", 100, 6000, 23),
    Wife("曾柔", 90, 6000, 23),
    Wife("方怡", 85, 4000, 26),
    Wife("沐剑屏", 86, 6000, 24),
    Wife("沐剑屏", 86, 6000, 24)
]
# 过滤器
for i in filter(lambda item: item.face_score > 90, list_wifes):
    print(i.name)

# 映射(一一对应)
for i in map(lambda item: (item.name, item.face_score), list_wifes):
    print(i)
# 排序sort(不改变原列表,boot值决定是否反转,默认为不反转)
for i in sorted(list_wifes, key=lambda item: item.face_score):
    print(i)
# 查找最大值/最小值
result = max(list_wifes, key=lambda item: item.money)
print(result.name)
from common_model.iterable_tools import IterableHepler
IterableHepler.delete(list_wifes,lambda item:item.name)
for i in list_wifes:
    print(i.name)