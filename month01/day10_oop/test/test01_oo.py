class Enemy:
    def __init__(self, name, hp, defense, atack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.atack = atack

    def injured(self, a):
        if a.atack - self.defense > 0:
            self.hp -= a.atack - self.defense
            if self.hp < 0:
                self.hp = 0
        else:
            self.hp -= 1
        print(self.name,"被攻击了,当前血量为",self.hp)

    def print_self(self):
        print(self.name, self.hp, self.defense, self.atack)

# f1 = Enemy("ww", 100, 50, 90)
# f2 = Enemy("ee", 0, 40, 30)
# f1.injured(f2)
# f1.print_self()
list_enemy = [
    Enemy("ww", 100, 50, 90),
    Enemy("ee", 40, 40, 100),
    Enemy("rr", 60, 40, 100)
]
def show():
    for i in range(len(list_enemy)-1):
        list_enemy[i].injured(list_enemy[i+1])
show()
for i in list_enemy:
    i.print_self()
# list_all = []
# list_all02 = []
# for i in list_enemy:
#     if i.hp > 0:
#         list_all.append(i)
#     if i.atack > 50:
#         list_all02.append(i)
# for i in list_all:
#     i.print_self()
# for i in list_all02:
#     print(i.name, i.atack)
