"""
作业
1. 三合一
2. 当天练习独立完成
3. 改造day07/exercise03代码
    定义函数,将二维列表以表格状打印出来
4. 改造day07/exercise06代码
    定义函数,判断列表中是否具有相同元素。
5. 定义函数,判断二维列表中是否具有某个元素
   例如：在list01中是否具有8
    list01 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
    ]
6. (扩展)方阵转置(不用做函数)
    思想：对角线不变,两端交换。
"""


# 3
def print_list(list_target):
    """

    :param list_target: list型--->传递一个二维列表
    :return:二维列表以表格状打印出来
    """
    # print(list_target)
    for i in range(len(list_target)):
        for j in range(len(list_target[i])):
            print(list_target[i][j], end="\t")
        print()


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print_list(list01)


# 4
def del_again(list_target):
    """

    :param list_target: list型--->传递一个列表
    :return:返回删除相同元素的列表
    """
    for i in range(len(list_target) - 1, 0, -1):
        for j in range(i):
            if list_target[i] == list_target[j]:
                list_target.remove(list_target[i])
                break
    return list_target


list01 = [34, 8, 56, 9, 8, 9]
print(del_again(list01))


# 5
def exit_number(list_target, number):
    """

    :param list_target: list型--->传递一个二维列表
    :param number: int型--->传递一个要判断的数字
    :return: 返回一个字符型--->"存在该数字" or  "该数字不存在"
    """
    for i in list_target:
        for j in i:
            if number == j:
                return "存在该数字"
    else:
        return "该数字不存在"


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(exit_number(list01, 15))

# 6
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for i in range(len(list01)-1):
    for j in range(i + 1, len(list01)):
        list01[i][j], list01[j][i] = list01[j][i], list01[i][j]
print(list01)
