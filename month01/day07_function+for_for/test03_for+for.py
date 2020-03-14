"""
    test03_for+for
    排序(升序)
"""
list01 = [4, 54, 5, 6, 7, 8, 3]
# list01 = [4, 15, 12, 9, 45, 33]
for i in range(len(list01) - 1):  # 最后一个不需要比较
    for j in range(i + 1, len(list01), 1):  # 不用判断自己和自己比较
        # print(list01)
        if list01[i] > list01[j]:
            list01[i], list01[j] = list01[j], list01[i]
print(list01)
