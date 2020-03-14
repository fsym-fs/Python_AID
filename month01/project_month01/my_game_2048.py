"""
    2048 核心算法
"""


# list_merge = [2, 0, 2, 0]
# list_merge = [2, 0, 8, 4]


# 1.定义函数,将list_merge里的0元素移动到末尾
def step_list(list_merge):
    """
    将list_merge里的0元素移动到末尾
    :param list_merge: list型--->用于存放一个列表
    :return:返回将list_merge里的0元素移动到末尾后的列表
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            list_merge.append(0)
            list_merge.remove(list_merge[i])


# print(step_list([2, 0, 0, 0, 0, 2, 0, 4]))

# 2.定义函数,将lis_merge里相同元素合并
def merge_list(list_merge):
    """

    :param list_merge:list型--->用于存放一个列表
    :return:返回lis_merge里相同元素合并后d的列表
    """
    # 调用step_list函数,先进行将0移到末尾
    step_list(list_merge)
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] = list_merge[i] * 2
            del list_merge[i + 1]
            list_merge.append(0)
    #         list_merge[i + 1] = 0
    # # 调用step_list函数,进行将0移到末尾,返回格式
    # step_list(list_merge)


# list01 = [2, 2, 2, 2]
# merge_list(list01)
# print(list01)
map = [
    [2, 0, 0, 2],
    [0, 4, 0, 2],
    [0, 4, 2, 0],
    [2, 0, 2, 0]
]


# 3.定义函数,将整个列表向左移动
def move_left(map):
    """
    将整个2048(4*4)列表向左移动
    :param map:list型 一个二维列表(4*4)向左移动后的界面
    :return:返回是
    """
    for every_list in map:
        merge_list(every_list)


# all_left_step(map)
# print(map)

# 定义函数,将map向右移动
def move_right(map):
    for every_list in map:
        # print(list_merge)
        for i in range(len(every_list) // 2):
            every_list[i], every_list[len(every_list) - 1 - i] = every_list[len(every_list) - 1 - i], every_list[i]
        merge_list(every_list)
        for i in range(len(every_list) // 2):
            every_list[i], every_list[len(every_list) - 1 - i] = every_list[len(every_list) - 1 - i], every_list[i]


# transpose
def transpose(map):
    for i in range(len(map) - 1):
        for j in range(i + 1, len(map)):
            map[i][j], map[j][i] = map[j][i], map[i][j]


def move_up():
    transpose(map)
    move_left(map)
    transpose(map)


def move_down():
    transpose(map)
    move_right(map)
    transpose(map)
