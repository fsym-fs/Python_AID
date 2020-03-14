"""
    定义函数,在列表中找出大于10的数字
    使用传统方法遍历列表
    使用生成器遍历列表
"""
list01 = [3, 42, 34, 435, 5, 64, 5, 67]
list02 = []
for i in list01:
    if i > 10:
        list02.append(i)
print(list02)


def get_number():
    for i in list01:
        if i > 10:
            yield i


result = get_number()
for i in result:
    print(i)
