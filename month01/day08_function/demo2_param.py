"""
param
    函数参数
        形式参数
"""


# 位置形参:必须传递
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 默认形参:从右向左,依次出现,不传递则使用默认值(可选)
def func01(p1=True, p2="", p3=0):
    print(p1)
    print(p2)
    print(p3)


# func01()
# func01(False,"a",10)
func01(False, p3="A")


# 星号元组形参
def func03(*p1):
    print(p1)


func03()
func03(34, 15, 16)
func03(*[1, 2, 3, 4])
func03([1, 2, 3, 4])


# 命名关键字形参
def func04(*args, p1=10, p2=20):
    print(*args)
    print(p1)
    print(p2)


def func05(p1, *, p2):
    print(p1)
    print(p2)


func05(1, p2=2)
func05(p1=1, p2=2)


# 双星号字典实参
def func06(**kwargs):
    print(kwargs)


func06(a=1, b=2)
func06()
