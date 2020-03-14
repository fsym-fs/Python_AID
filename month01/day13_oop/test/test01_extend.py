"""
一家公司有如下几种岗位:
    程序员:底薪+项目分红
    测试员:底薪+bug*5
    .....
创建员工管理器
    记录所有员工
    提供计算总工资的功能
叙述:
    三大特征:
        封装:根据需求划分为员工管理器,程序员测试类
        继承:创建员工类,隔离员工管理器和具体员工的变化
        多态:员工管理器调用父类(员工)--->具体员工重写员工类的计算薪资方法--->添加具体员工对象方法
                  调父                        重写                        创建子对象
             总结:
                步骤:面对变化点,需要使用3步进行处理
                价值(作用):程序灵活(扩展性强 = 开闭原则)
    六大原则:
        开闭原则:增加员工种类,员工管理器代码不变
        单一职责:员工管理器:统一管理所有员工
                程序员:为了定义该员工的薪资算法
                测试员:为了定义该员工的薪资算法
        依赖倒置:员工管理器调用员工类,不调用具体员工类
        组合复用:优先选择组合:员工管理器通过组合关系,使用具体员工的薪资算法
        里氏替换:向员工管理器添加的是员工类的子类对象--->子类重写员工类,先调用员工类的计算薪资方法,返回底薪,在添加自己的其他工资
        迪米特:每个具体员工类之间低耦合,员工管理器和具体员之间低耦合
"""


class Staff_manager:
    result = 0

    def __init__(self):
        self.list_manager = []

    def record(self, staff):
        wage = staff.wage()
        self.list_manager.append({staff.name: wage})
        Staff_manager.result += wage
        print(self.list_manager, Staff_manager.result)


class Staff:
    def __init__(self, base_salary, name):
        self.base_salary = base_salary
        self.name = name

    def wage(self):
        return self.base_salary


class Programmer(Staff):

    def __init__(self, base_salary, share_out_bonus, name):
        super().__init__(base_salary, name)
        self.share_out_bonus = share_out_bonus

    def wage(self):
        return super().wage() + self.share_out_bonus


class Tester(Staff):

    def __init__(self, base_salary, bug_number, name):
        super().__init__(base_salary, name)
        self.bug_number = bug_number

    def wage(self):
        return super().wage() + 5 * self.bug_number


a = Staff_manager()
p = Programmer(100, 1000, "hh")
t = Tester(50, 10, "gg")
a.record(p)
a.record(t)
