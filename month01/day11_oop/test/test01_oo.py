"""
小明在银行去钱
人的钱多了,银行的钱少了
"""


class Person:

    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount

    # def get_money(self, bank, number):
    #     self.number = number
    #     bank.draw_money(self)
    #     print(self.name, "去", bank.name, "取出", self.number, "元", sep="")
    #     self.amount += self.number


class Bank:
    amount = 100000

    def __init__(self, name):
        self.name = name

    def draw_money(self, person,number):
        Bank.amount -= number
        print(self.name, "被取出", number, "元", sep="")
        person.amount += number


xm = Person("小明")
bank = Bank("三峡银行")
# xm.get_money(bank)
bank.draw_money(xm,100)
# print(xm.amount)
