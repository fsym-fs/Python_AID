"""
test05_function
    质数:大于1,除了被自身和1整除以外,不能被其他数字整除
"""


def judge_prime_numbers(number):
    """
    判断数是否为质数
    :param number:int型
    :return:是质数返回该数,不是返回0
    """
    for i in range(2, number):
        if number % i == 0:
            return 0
    return number


def scope(start_number, end_number):
    """
    在范围内循环添加范围内的质数
    :param start_number:int型,开始位置
    :param end_number:int型,结束位置
    :return:返回存放范围内质数的列表
    """
    return [i for i in range(start_number, end_number + 1) if judge_prime_numbers(i)]
    # list_number = []
    # for i in range(start_number, end_number + 1):
    #     if judge_prime_numbers(i):
    #         list_number.append(i)
    # return list_number


print(scope(2, 20))
