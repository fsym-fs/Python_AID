# """
#     张无忌教赵敏九阳神功
#     赵敏教张无忌化妆
#     张无忌上班挣了8000
#     赵敏上班挣了10000
# """
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def teach(self, person, skill):
#         print(self.name, "教", person.name, skill.name, sep="")
#         # job.earn(self.name,8000)
#
#
# class Skills:
#     def __init__(self, name):
#         self.name = name
#
#
# class Job:
#     def earn(self, person, money):
#         print(person.name, "挣了", money, "元", sep="")
#
#
# p1 = Person("张无忌")
# p2 = Person("赵敏")
# s1 = Skills("九阳神功")
# s2 = Skills("化妆")
# p1.teach(p2, s1)
# p2.teach(p1, s2)
# j1 = Job()
# j1.earn(p1, 8000)
# j2 = Job()
# j2.earn(p2, 10000)
class Person:
    def __init__(self, name, skill, money=0):
        self.name = name
        self.skill = skill
        self.money = money

    def teach(self, person):
        print(self.name, "教", person.name, self.skill, sep="")

    def earn(self):
        print(self.name, "挣了", self.money, "元", sep="")


p1 = Person("张无忌", "九阳神功", 8000)
p2 = Person("赵敏", "化妆", 10000)
p1.teach(p2)
p2.teach(p1)
p1.earn()
p2.earn()
