"""
test02_function
"""


def del_again(list_targent):
    """
        删除列表中的删除元素
    :param list_targent:
    """
    for i in range(len(list_targent) - 1, 0, -1):
        for j in range(i):
            if list_targent[i] == list_targent[j]:
                list_targent.remove(list_targent[i])
                break


list01 = [34, 8, 56, 9, 8, 9]
del_again(list01)
print(list01)
