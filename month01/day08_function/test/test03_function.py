"""
test03_function
"""


def sort_list(list_target):
    """
    排序(升序)
    :param list_target:
    :return:
    """
    for i in range(len(list_target) - 1):  # 最后一个不需要比较
        for j in range(i + 1, len(list_target), 1):  # 不用判断自己和自己比较
            # print(list01)
            if list_target[i] > list_target[j]:
                list_target[i], list_target[j] = list_target[j], list_target[i]


list01 = [4, 54, 5, 6, 7, 8, 3]
sort_list(list01)
print(list01)
