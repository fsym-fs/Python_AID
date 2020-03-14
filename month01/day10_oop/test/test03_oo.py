"""
    对象计数器
"""


class Wife:
    __count = 0

    def __init__(self, name):
        self.name = name
        Wife.__count += 1

    @classmethod
    def show_count(cls):
        return cls.__count


w01 = Wife("1")
w01 = Wife("2")
w01 = Wife("3")
w01 = Wife("4")
w01 = Wife("5")
w01 = Wife("6")
w01 = Wife("7")
# print(Wife.__count)
print(Wife.show_count())
