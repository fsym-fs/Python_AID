# f = open("day03/test/1.txt","w")
# f.write("woshinibabab\n")
# f.write("qunidayede!\n")
# f.close()
# f = open("day03/test/1.txt","a")
# f.write("ququququ!\n'")
# f.close()
# f = open("day03/test/1.txt","a")
# f.writelines(["a","asdf"])
# f.close()
# with open("day03/test/1.txt","r") as f:
#     print(f.read())
"""
    拷贝文件
    编写一个函数，完成对文件的复制作用
"""


def copy(file1, file2):
    with open(file1, "rb") as f:
        with open(file2, "wb") as target:
            while True:
                a = f.read(1024)
                if not a:
                    break
                target.write(a)


copy("day03/test/ 1.txt", "day03/test/2.txt")
