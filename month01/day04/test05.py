"""
Test05
    累加10--80之间个位不是3/5/9的整数
"""
#1
result = 0
for i in range(10,81):
    if i%10==3 or i%10==5 or i%10==9:
        continue
    result +=i
print(result)

#2
result = 0
a = [3,5,9]
for i in range(10,81):
    if i%10 in a:
        continue
    result +=i
print(result)