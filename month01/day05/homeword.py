"""
    作业
    1. 三合一
    2. 当天练习独立完成
    3. 画出下列代码内存图
    list01 = [
        1,2,3,
        [4,5,6]
    ]
    list02 = list01
    list03 = list01[::]
    list02[0] = [7,8,9]
    list03[0:1] = [9,10,11]
    list03[1][0] = "悟空"
    print(list01)
    print(list02)
    print(list03)
    4. 彩票：双色球
        蓝色：6个  1-33之间整数  不能重复
        红色：1个  1-16之间整数
    -- 随机创建一注彩票（列表,红色作为最后一个元素）
    -- 在终端中录入（购买）一注彩票
        提示："请输入第1个蓝色号码"   "数字超过范围"   "号码已经存在"
    5. 阅读
        程序员的数学 第五章  排列组合
"""
import random

number_list = []
i = 1
while True:
    if i != 7:
        number = random.randint(1, 34)
        if number not in number_list:
            number_list.append(number)
            i += 1
        else:
            continue
    else:
        number = random.randint(1, 17)
        number_list.append(number)
        break
print(number_list)
