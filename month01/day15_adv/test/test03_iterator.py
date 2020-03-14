"""
    ("悟空","八戒","唐僧"):利用迭代思想遍历元组
    {"悟空":101,"八戒":102,"唐僧":103}(获取字典里的所有元素,但不可以使用for循环)
"""
tuple01=("悟空","八戒","唐僧")
a = tuple01.__iter__()
while True:
    try:
        print(a.__next__())
    except StopIteration:
        break
dict01 = {"悟空":101,"八戒":102,"唐僧":103}
print("------------------------------------------")
b = dict01.__iter__()
while True:
    try:
        t = b.__next__()
        print(t,dict01[t])
    except StopIteration:
        break