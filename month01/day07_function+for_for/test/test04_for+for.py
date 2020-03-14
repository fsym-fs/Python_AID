"""
test04_for+for
    list01 = [34,8,56,9,8,9]
    判断是否有相同元素
"""
result = 0
list01 = [34, 8, 56, 9, 8, 9]
for i in range(len(list01) - 1):
    for j in range(i + 1, len(list01), 1):
        if list01[i] == list01[j]:
            result += 1
            break
    if result != 0:
        print("有相同的元素")
        break
if result == 0:
    print("没有相同元素")
