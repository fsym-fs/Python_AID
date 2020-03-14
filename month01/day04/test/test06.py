"""
Test06
    chr与ord(解码与编码)
            26446
            28165
            28165
    1.在终端中获取一个字符串,打印出每个文字的编码值
    2.在终端循环输入编码值,打印每个文字
        要求:如果录入空字符,则退出程序
"""
n = input("输入一个字符串:")
for i in n:
    print(ord(i),end="  ")
print("")
while True:
    s = input("输入编码值:")
    if s=="":
        break
    elif s==" ":
        break
    else:
        code = int(s)
        print(chr(code))
