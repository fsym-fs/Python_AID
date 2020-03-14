"""
test06_function
"""


class test06_function:
    """
        关于函数的练习
    """

    def show_list(self, list_number):
        """
        定义函数,在终端中打印列表(一行一个)

        :param(参数):list类型-->list_number
        :return:列表的每一个元素(一行一个)
        """
        for i in list_number:
            print(i)


f = test06_function()
# 定义实参
list01 = [43, 4, 5, 78]
list02 = [76, 6, 579]
# 调用show_list函数
f.show_list(list01)
f.show_list(list02)
