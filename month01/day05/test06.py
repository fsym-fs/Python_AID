"""
Test06
    在终端中循环录入字符串,若为空,则停止
    打印所有录入的内容(一个字符串)
"""
l = []
while True:
    try:
        n = input("输入字符串:")
        if n == "":
            break
        else:
            l.append(n)
    except:
        break
print("".join(l))