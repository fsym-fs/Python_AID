"""
test05_for+for
    list01 = [34,8,56,9,8,9]
    删除列表相同的元素(只保留一个)
"""
list01 = [34, 8, 56, 9, 8, 9]
for i in range(len(list01) - 1, 0, -1):
    for j in range(i):
        if list01[i] == list01[j]:
            list01.remove(list01[i])
            break
print(list01)
