"""
    属性练习:
        创建敌人类
            数据:
                姓名
                血量(0--500)
                攻击力(10-100)
        创建敌人对象,体会拦截的核心逻辑
"""


class Enemy:
    # __hp = 0
    def __init__(self, name, hp, atack):
        self.name = name
        self.hp = hp
        self.atack = atack


    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, values):
        if values >= 0 and values <= 500:
            self.__hp = values
        else:
            raise Exception("程序错误!")

    @property
    def atack(self):
        return self.__atack

    @atack.setter
    def atack(self, values):
        if values >= 10 and values <= 100:
            self.__atack = values
        else:
            raise Exception("程序错误!")
    # hp = property(get_hp, set_hp)
    # atack = property(get_atack, set_atack)


f = Enemy("hh", 100, 50)
# print(f.hp)
# f.hp = 10000
# print(Enemy.hp)
