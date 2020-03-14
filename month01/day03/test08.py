"""
Test08
    在终端中显示0 1 2
    在终端中显示6 7 8 9 10
    在终端中显示2 4 6 8
    在终端中显示9 8 7 6 5 4 3
    在终端中显示-1 -2 -3 -4 -5 -6
"""
#end=""结尾可以实现不换行输出
i =0
while i<3:
    print(i,end="")
    i+=1
print("------------")
i = 6
while i<11:
    print(i,end="")
    i+=1
print("------------")
i = 2
while i<9:
    print(i,end="")
    i+=2
print("------------")
i = 9
while i>2:
   print(i,end="")
   i -= 1
print("------------")
i = -1
while i >-7:
    print(i,end="")
    i-=1