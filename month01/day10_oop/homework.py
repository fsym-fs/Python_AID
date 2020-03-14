"""
作业
1. 三合一
2. 当天练习独立完成
3. 创建技能类
     数据:技能名称、持续时间(1-60)、攻击力(0-500)、消耗法力(0--1000)

   创建技能列表(3个以上)
   定义函数实现下列功能：
   -- 在技能列表中查找攻击力大于100的所有技能名称,攻击力与消耗的法力
   -- 在技能列表中查找消耗法力最大的技能对象
   -- 在技能列表中删除持续时间大于50的技能对象
   -- 根据消耗的法力对技能列表进行升序排列
   -- 将技能列表中攻击力小于100的技能消耗法力设置为0
   -- 删除技能列表中持续时间相同的技能(只保留一个)
"""


class Skills:
    """
    技能类
        数据:技能名称、持续时间(1-60)、攻击力(0-500)、消耗法力(0--1000)

    创建技能列表(3个以上)
        定义函数实现下列功能：
            -- 在技能列表中查找攻击力大于100的所有技能名称,攻击力与消耗的法力
            -- 在技能列表中查找消耗法力最大的技能对象
            -- 在技能列表中删除持续时间大于50的技能对象
            -- 根据消耗的法力对技能列表进行升序排列
             -- 将技能列表中攻击力小于100的技能消耗法力设置为0
            -- 删除技能列表中持续时间相同的技能(只保留一个)
    """

    def __init__(self, name, time, attack, mp):
        self.name = name
        self.time = time
        self.attack = attack
        self.mp = mp

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, values):
        if values >= 1 and values <= 60:
            self.__time = values
        else:
            raise Exception("程序错误!")

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, values):
        if values >= 0 and values <= 500:
            self.__attack = values
        else:
            raise Exception("程序错误!")

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, values):
        if values >= 0 and values <= 1000:
            self.__mp = values
        else:
            raise Exception("程序错误!")

    def show_all(self):
        print(self.name, self.time, self.attack, self.mp)


list_skills = [
    Skills("摩诃无量", 55, 217, 60),
    Skills("天下无狗", 8, 270, 50),
    Skills("小无相功", 2, 80, 10),
    Skills("天下无狗", 8, 270, 50),
    Skills("罗汉棍", 2, 200, 10),
    Skills("迦叶功", 5, 150, 20),
    Skills("神龙摆尾", 2, 200, 10),
    Skills("亢龙有悔", 20, 200, 40)
]


# 在技能列表中查找攻击力大于100的所有技能名称,攻击力与消耗的法力


def find_attack(list_skills):
    list_attack = []
    for skill in list_skills:
        if skill.attack > 100:
            list_attack.append(skill)
    return list_attack


# 在技能列表中查找消耗法力最大的技能对象
def max_mp(list_skill):
    list_max_mp = []
    max_mp = list_skills[0]
    for i in range(1, len(list_skills)):
        if max_mp.mp < list_skills[i].mp:
            max_mp = list_skills[i]
    for skill in list_skills:
        if skill.mp == max_mp.mp:
            list_max_mp.append(skill)
    return list_max_mp


# 在技能列表中删除持续时间大于50的技能对象
def del_skill(list_skills):
    for i in range(len(list_skills) - 1, -1, -1):
        if list_skills[i].time > 50:
            del list_skills[i]
    return list_skills


# 根据消耗的法力对技能列表进行升序排列
def sort_skills(list_skills):
    for i in range(len(list_skills) - 1):
        for j in range(i + 1, len(list_skills)):
            if list_skills[i].mp > list_skills[j].mp:
                list_skills[i], list_skills[j] = list_skills[j], list_skills[i]
    return list_skills


# 将技能列表中攻击力小于100的技能消耗法力设置为0
def set_attack(list_skills):
    for skill in list_skills:
        if skill.attack < 100:
            skill.attack = 0
    return list_skills


# 删除技能列表中持续时间相同的技能(只保留一个)
def del_s(list_skills):
    for i in range(len(list_skills)-1):
        for j in range(len(list_skills) - 1, i, -1):
            if list_skills[i].time == list_skills[j].time:
                del list_skills[j]
                # break
    return list_skills


# result = del_skill(list_skills)
# result = max_mp(list_skills)
# result = find_attack(list_skills)
# result = sort_skills(list_skills)
# result = set_attack(list_skills)
# result = del_s(list_skills)
# for skill in result:
#     skill.show_all()
