"""
    创造一个技能类(名称,持续时间(0--60))
    如果持续时间超过范围,传递错误信息(信息/编号/代码)
"""


class SkillError(Exception):
    def __init__(self, message="", id=0, code=""):
        self.message = message
        self.id = id
        self.code = code


class Skill:
    def __init__(self, name="", time=0):
        self.name = name
        self.time = time

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if value <= 60 and value >= 0:
            self.__time = value
        else:
            raise SkillError("技能持续时间不在0--60之内", 1001, "if value <=60 and value >=0")


try:
    s = Skill("天下无狗", 80)
except SkillError as e:
    print("程序错误!")
    print(e.id, e.message, e.code)
