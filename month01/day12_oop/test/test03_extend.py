"""
    手雷爆炸,可能伤害玩家,敌人生命,还可能伤害房子,鸭子.....
    要求,增加新事物,不影响手雷类
"""


class Hand_grenades:
    def explosion(self, thing):
        print("手雷爆炸啦!!!!!!!!")
        thing.injured()


class Things:
    def injured(self):
        pass


# -----------------------------------------------------------------------------------------------------------------------------------------------

class Players(Things):
    def injured(self):
        print("您受到手雷攻击,血量扣除50点!")


class Enemy(Things):
    def injured(self):
        print("敌人受到手雷攻击,血量扣除100点!")


class House(Things):
    def injured(self):
        print("房子受到手雷攻击,破损度扣20%!")


class Duck(Things):

    def injured(self):
        print("鸭子受到手雷攻击,扣除100%血量,已经死亡!")


class Batman(Things):

    def injured(self):
        print("小兵受到手雷攻击,血量扣除50%!")


sl = Hand_grenades()
p1 = Players()
e1 = Enemy()
d1 = Duck()
h1 = House()
sl.explosion(p1)
sl.explosion(e1)
sl.explosion(d1)
sl.explosion(h1)
b1 = Batman()
sl.explosion(b1)
