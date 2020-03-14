# class SkillIterator:
#     def __init__(self, data):
#         self.__data = data
#         self.__index = -1
#
#     def __next__(self):
#         self.__index += 1
#         if self.__index > len(self.__data) - 1:
#             raise StopIteration()
#         return self.__data[self.__index]


class SkillManager:
    def __init__(self):
        self.__all_skills = []

    def add_skill(self, skill):
        self.__all_skills.append(skill)

    def __iter__(self):
        # return SkillIterator(self.__all_skills)
        """
            yield标记此时程序需一分为二
            生成迭代器代码的大致逻辑:
                1.将yield语句以前的代码,定义到next方法体中
                2.将yield语句以后的数据,作为next方法的返回值
        """
        for i in self.__all_skills:
            yield i
        # for i in range(len(self.__all_skills)):
        #     yield self.__all_skills[i]


manager = SkillManager()
manager.add_skill("降龙十八掌")
manager.add_skill("六脉神剑")
manager.add_skill("猴子偷桃")

# for item in manager:
#     print(item)

# for item in manager:
#     print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
