"""
    创建员工管理器
    记录多个员工
    迭代员工管理器,打印多个员工
    画出架构设计图
"""


class Staff_iterator:
    def __init__(self, list01):
        self.list01 = list01
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index > len(self.list01) - 1:
            raise StopIteration
        return self.list01[self.index]


class Staff_merage:
    def __init__(self):
        self.staff_list = []

    def addstaff(self, staff):
        self.staff_list.append(staff)

    def __iter__(self):
        return Staff_iterator(self.staff_list)


class Staff:
    def __init__(self, name):
        self.name = name

    def doing(self):
        pass


"""
-----------------------------------------------------------------------------------------------------
"""


class Staff_1(Staff):
    def __init__(self, name):
        super().__init__(name)

    def doing(self):
        super().doing()
        print("111")


class Staff_2(Staff):
    def __init__(self, name):
        super().__init__(name)

    def doing(self):
        super().doing()
        print("222")


st = Staff_merage()
st.addstaff(Staff_1("1"))
st.addstaff(Staff_2("2"))
s_iterable = st.__iter__()
while True:
    try:
        b = s_iterable.__next__()
        print(b.name, end=":")
        b.doing()
    except StopIteration:
        break
