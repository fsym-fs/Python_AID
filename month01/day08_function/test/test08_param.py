"""
Test
    定义函数,数值相加
"""


def account_number(*number_args):
    """
    :param number_args:合并传递的参数为一个元组
    :return: 返回数值相加
    """
    try:
        s = 0
        for i in number_args:
            s += float(i)
        return s
    except:
        return "程序错误!"


print(account_number())
print(account_number(1, 2))
print(account_number(1, 2, 5, 84, 6))
print(account_number(*[1, 2, 5, 84, 6]))
print(account_number([1, 2, 5, 84, 6]))
