"""
test04_function
    根据月份计算天数
"""


def judge_February(year):
    """

    :param year:int 型获取年份
    :return:如果是闰年返回True
    """
    return int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0


def account_day(year, month):
    """

    :param year:int型--->输入一个年份
    :param month:int型--->输入一个月份
    :return:返回该年该月的天数
    """
    month = int(month)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
        # return "%d年%d月有%d天" % (year, month, 31)
    if month in [2]:
        return 29 if judge_February(year) else 28
        # if judge_February(year):
        #     return "%d年%d月有%d天" % (year, month, 29)
        # else:
        #     return "%d年%d月有%d天" % (year, month, 28)
    if month < 1 or month > 12:
        return "输入错误(1-12)"
    else:
        return 30
        # return "%d年%d月有%d天" % (year, month, 30)


print(account_day(2020, 11))
