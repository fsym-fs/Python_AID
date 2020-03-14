"""
param
    函数参数
        实际参数
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


#
# # 位置实参
# func01(1, 2, 3)
#
# # 序列实参(拆再对应)
# list01 = ["a", "b", "c"]
# dict01 = {"a": 1, "b": 2, "c": 3}
# func01(*dict01)
#
# # 关键字实参
# func01(p2=10, p1=100, p3=5)

# 字典实参
dict01 = {"p1": 1, "p2": 2, "p3": 3}
func01(**dict01)
