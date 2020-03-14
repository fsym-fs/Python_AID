"""
    创建图形管理器
        记录图形面积
        圆形:pi*r**2
        矩形:l*w
    写出:
        三大特征
            封装:通过不同的图形对应不同的计算方法,所以,以图形进行划分
            继承:创建图形类,隔离图形管理器和具体图形的面积的变化
            多态:具体图形计算方法不同,则图形管理器,调用图形,执行圆,矩形的计算方法
                通过重写做具体图形计算面积的方法
        设计原则
            开闭原则:增加新图形,图形管理器不变
            依赖倒置:图形管理器,调用图形,不调用具体图形类
"""


class Graphic_manager:
    def __init__(self, list_graphic):
        self.__list_area = []
        self.__list_graphic = list_graphic

    def __calculate_area(self):
        r = 0
        for graphic in self.__list_graphic:
            s = graphic.calculate_area()
            r += s
            self.__add_graphic({graphic.name: s})
        print(r)

    def __add_graphic(self, s):
        self.__list_area.append(s)

    def __show_all(self):
        for i in self.__list_area:
            print(i)

    def main(self):
        self.__calculate_area()
        self.__show_all()


class Graphic:
    def __init__(self, name):
        self.name = name

    def calculate_area(self, name):
        pass


# ----------------------------------------------------------------------------------------------------------------------------------------------

class Circular(Graphic):
    def __init__(self, r, name):
        super().__init__(name)
        self.r = r
        self.name = name

    def calculate_area(self):
        return 3.14 * float(self.r) ** 2


class Rectangular(Graphic):
    def __init__(self, height, width, name):
        self.height = height
        self.width = width
        super().__init__(name)

    def calculate_area(self):
        return float(self.height) * float(self.width)


list_01 = [
    Circular(2, "圆形"),
    Rectangular(2, 3, "矩形")
]
g = Graphic_manager(list_01)
g.main()
