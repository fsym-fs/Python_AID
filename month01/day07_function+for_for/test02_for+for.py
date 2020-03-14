"""
test02_for-for..
"""
#1
for i in range(4):
    for j in range(5):
        if i%2:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()

# 2
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# 打印第三行第二列的数据
print(list01[2][1])
# 从右到左打印第二行数据(一行一个)
for j in range(len(list01[1]) - 1, -1, -1):
    print(list01[1][j])
# 从上到下打印第三列的数据(一行一个)
for i in range(len(list01)):
    print(list01[i][2])
# 将二维数组一表格形式打印
    #1
for line in list01:
    for item in line:
        print(item, end=" ")
    print()
    #2
for i in range(len(list01)):
    for j in range(len(list01[i])):
        print(list01[i][j], end=" ")
    print()

#3转置矩阵
list02 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
list03=[]
for i in range(len(list02[1])):
    list04 = []
    for j in range(len(list02)):
        list04.append(list02[j][i])
    list03.append(list04)
print(list03)

#4
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()

#5
for i in range(4):
    for j in range(0,4,1):
        if j>=i:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

#6
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()

#7
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d "%(j,i,i*j),end=" ")
    print()
