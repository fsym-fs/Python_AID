"""
    iterator
    创建图形管理器,
    记录多个图形,
    迭代图形管理器,打印多个图形
"""


class graphicsiterator:
    def __init__(self, list01):
        self.list01 = list01
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index > len(self.list01) - 1:
            raise StopIteration
        return self.list01[self.index]


class graphicsManager:
    def __init__(self):
        self.list_graphics = []

    def addgraphics(self, skill):
        self.list_graphics.append(skill)

    def __iter__(self):
        return graphicsiterator(self.list_graphics)


g = graphicsManager()
g.addgraphics("11")
g.addgraphics("22")
a = g.__iter__()
while True:
    try:
        b = a.__next__()
        print(b)
    except StopIteration:
        break
