"""
    1. 在技能列表中，查找所有技能的名称name,攻击力atk与消耗法力cost_sp
    2. 在技能列表中,查找攻击力大于200的所有技能对象
    3. 在技能列表中,查找持续时间小于50的所有技能名称
    4. 在列表中找出最短的元素[(1,1),(2,),(3,3,3),(4,4)]
    5. 根据消耗法力对技能列表进行降序排列.
"""


class Skill:
    def __init__(self, name="", duration=0, atk=0, cost_sp=0):
        self.name = name
        self.duration = duration
        self.atk = atk
        self.cost_sp = cost_sp


list_skills = [
    Skill("乾坤大挪移", 50, 200, 500),
    Skill("降龙十八掌", 60, 300, 800),
    Skill("金钟罩", 60, 0, 200),
    Skill("猴子偷桃", 10, 150, 0),
]

# 在技能列表中，查找所有技能的名称name,攻击力atk与消耗法力cost_sp
for item in map(lambda item: (item.name, item.atk, item.cost_sp), list_skills):
    print(item)
# 在技能列表中,查找攻击力大于200的所有技能对象
for item in filter(lambda item: item.atk > 200, list_skills):
    print(item.__dict__)
# 在技能列表中,查找持续时间小于50的所有技能名称
for item in map(lambda item: item.name, filter(lambda item: item.duration < 50, list_skills)):
    print(item)
# 在列表中找出最短的元素[(1,1),(2,),(3,3,3),(4,4)]
result = min([(1, 1), (2,), (3, 3, 3), (4, 4)], key=lambda item: len(item))
print(result)
# 根据消耗法力对技能列表进行降序排列.
for item in sorted(list_skills, key=lambda item: item.cost_sp, reverse=True):
    print(item.__dict__)
