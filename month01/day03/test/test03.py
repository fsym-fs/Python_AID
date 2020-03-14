"""
Test03
    录入4个同学的体重
    打印最重的体重
    算法:

"""

"""
    1
"""
Max_weight = 0
print("输4名入同学的体重:")
for i in range(0, 4, 1):
    weight = int(input())
    if weight > Max_weight:
        Max_weight = weight
print("Max_weight=" + str(Max_weight))

"""
    2
"""
Max_weight = 0
weight_01 = int(input("输入同学的体重:"))
weight_02 = int(input("输入同学的体重:"))
weight_03 = int(input("输入同学的体重:"))
weight_04 = int(input("输入同学的体重:"))
if weight_01 > Max_weight:
    Max_weight = weight_01
if weight_02 > Max_weight:
    Max_weight = weight_02
if weight_03 > Max_weight:
    Max_weight = weight_03
if weight_04 > Max_weight:
    Max_weight = weight_04
print("Max_weight=" + str(Max_weight))

"""
    3
"""
Max_weight = 0
weight_list = []
weight = input("输4名入同学的体重:")
weight_list = weight.split()
print("Max_weight:" + str(max(weight_list)))