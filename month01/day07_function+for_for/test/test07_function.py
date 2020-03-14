"""
test07_function
"""


class test07_function:
    """
        关于函数的练习
            定义函数,在终端中根据边长打印矩形
    """

    def print_rectangle(self, length, str_symbol):
        """
        定义函数,传递两个参数,根据边长和边长的符号打印矩形

        :param length:int型-->边长

                str_symbal:字符型--->边长的形状

        :return:边长为参数值的矩形
        """
        for i in range(0, length, 1):
            if i == 0 or i == length - 1:
                print(str_symbol * length)
            else:
                print(str_symbol + " " * (length - 2) + str_symbol)


f = test07_function()
length = int(input("输入一个矩形边长:"))
f.print_rectangle(length, "^")
