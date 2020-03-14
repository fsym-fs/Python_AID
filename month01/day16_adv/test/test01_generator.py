"""
    参照enumeration自定义my_enumeration函数
    将list01中,长度大于2的元素设置为空字符串
"""
# list01 = ["唐僧", "猪八戒", "悟空"]
# dict01 = {"唐僧": 101, "猪八戒": 102, "悟空": 103}
# for i in enumerate(list01):
#     print(i)
#
#
# def my_enumeration(a):
#     index = 0
#     for item in a:
#         yield (index, item)
#         index += 1
#
#
# for i in my_enumeration(list01):
#     print(i)
# for i, k in my_enumeration(dict01.items()):
#     print(i, k)
"自定义my_zip函数"

list01 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in zip(*list01):
    print(i)

def my_zip(*args):
    li = []
    for i in range(len(args)):
        for j in range(len(args[i])):
            li.append(args[j][i])
        yield tuple(li)
        li = []
for i in my_zip(*list01):
    print(i)