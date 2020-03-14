
"""
Test
    定义函数,根据时分秒计算总秒数
    测试:
        时,分,秒--->
        时,分  --->
           分  --->
        时,  秒--->
"""


def account_seconds(hour=0, minutes=0, seconds=0):
    """
    根据时分秒计算总秒数
    :param hour:
    :param minutes:
    :param seconds:
    :return: 返回总秒数
    """
    try:
        if hour > 24 or hour < 0 or minutes > 60 or minutes < 0 or seconds > 60 or seconds < 0:
            return "输入错误"
        return hour * 60 * 60 + minutes * 60 + seconds
    except:
        return "程序错误!"


print(account_seconds(seconds=5))