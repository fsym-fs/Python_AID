"""
需求:
    玩家(攻击力)攻击敌人,敌人(血量)受伤后(减少血量),可能死亡(播放死亡动画)
"""


class Player:
    def __init__(self, name, attack):
        self.name = name
        self.__attack = attack

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def atttack(self, value):
        if value >= 0:
            self.__attack = value

    def attack_enemy(self, enemy):
        if enemy.hp > self.attack:
            enemy.hp -= self.attack
        else:
            enemy.hp = 0
        enemy.damage()


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value >= 0:
            self.__hp = value

    def damage(self):
        print("额,受伤了")
        if self.hp <= 0:
            self.__show_die()

    def __show_die(self):
        print("我死啦!")


xm = Player("小明", 100)
xw = Enemy("小王", 100)
xm.attack_enemy(xw)
