class File_io:
    """
        使用dict文件，完成单词的查找
        1.使用input 输入一个单词
        2.查找到这个单词，打印出该单词，及其解释
        3.每个单词占一行，单词与解释之间有空格
    """

    def __init__(self, name):
        self.name = name

    def file_read(self, func):
        f = open(self.name, "r")
        a = f.read()
        print(a)
        func(f)

    def file_read_b(self, func):
        f = open(self.name, "rb")
        a = f.read()
        print(a)
        func(f)

    def file_write(self, func):
        f = open(self.name, "w")
        f.write("qwe")
        func(f)

    def file_return(self, result):
        print(result)
        result.close()

    def file_read_n(self, func, n):
        f = open(self.name, "r")
        while True:
            data = f.read(n)
            if not data:
                break
            print(data)
        func(f)

    def file_read_line(self, func, n):
        f = open(self.name, "r")
        data = f.readline(n)
        print(data)
        data = f.readline(n)
        print(data)
        func(f)

    def file_read_lines(self, func, n=""):
        f = open(self.name, "r")
        data = f.readlines(n)
        print(data)
        func(f)

    """
        使用dict文件，完成单词的查找
        1.使用input 输入一个单词
        2.查找到这个单词，打印出该单词，及其解释
        3.每个单词占一行，单词与解释之间有空格
    """

    def file_line_all(self):
        n = input("输入一个单词:")
        for line in open(self.name, "r"):
            a = line.split(" ")
            if a[0] > n:
                return "查无此单词！" 
            elif n == a[0]:
                return line
        return "查无此单词！"


w = File_io("day03/test/dict.txt")
# w.file_read(w.file_return)
# # w.file_read_b()
# w.file_write(w.file_return)
# w.file_read_n(w.file_return, 1024)
# w.file_read_lines(w.file_return, 25)
print(w.file_line_all())
