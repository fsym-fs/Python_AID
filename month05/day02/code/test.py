"""
李白好饮酒，
无事街上走；
提壶去打酒，
原有酒两斗；
遇店加一倍，
遇花喝一斗。
    1、酒壶刚开始酒为2斗；

    2、遇到店酒的量会翻倍（*2），遇到话会喝一斗（-1）；

    3、总共遇到店5次，花10次。最后一次肯定是遇花；
"""
n = 2

# a = '花'
# b = '酒'
# c = '店'

i = 0
lis = []


def func(a, b, c, lis):
    print(a, b, c)
    if a == 1 and b == 1 and c == 0:
        # b -= 1
        global i
        i += 1
        print('111')
        # print(lis)
        return lis
    if c > 0 and b > 0:
        lis.append('店')
        func(a, b * 2, c - 1, lis)
    elif a > 1 and b > 0:
        lis.append('花')
        func(a - 1, b - 1, c, lis)


print(func(10, 2, 5, []))
# print(i)
