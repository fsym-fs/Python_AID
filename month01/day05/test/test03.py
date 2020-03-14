"""
Test03
    list01=[54,5,65,67,78,8]
    删除列表中的所有奇数(倒序删除)
    (内存:删除后,是从后往前覆盖)
"""
#1
list01=[54,5,65,67,78,8]
list02 = []
j = len(list01)
for i in range(0,j,1):
    if list01[i]%2!=0:
        list02.append(list01[i])
for i in list02:
    list01.remove(i)
print(list01)

#2
list01=[54,5,65,67,78,8]
list02 = []
j = len(list01)
for i in range(j-1,-1,-1):
    if list01[i]%2!=0:
        list01.remove(list01[i])
print(list01)
