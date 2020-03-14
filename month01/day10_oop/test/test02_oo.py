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
        print(self.name, "被攻击了,当前血量为", self.hp)

    def print_self(self):
        print(self.name, self.hp, self.defense, self.atack)


list_enemy = [
    Enemy("ww", 100, 50, 90),
    Enemy("ee", 0, 40, 100),
    Enemy("tt", 40, 50, 10),
    Enemy("yy", 0, 80, 30),
    Enemy("uu", 60, 60, 70)
]


def show_defense():
    min = list_enemy[0]
    for i in range(1, len(list_enemy) - 1):
        if min.defense > list_enemy[i].defense:
            min = list_enemy[i]
    min.print_self()


def del_atack():
    for i in range(len(list_enemy) - 1, -1, -1):
        if list_enemy[i].hp > 50:
            del list_enemy[i]
    for i in list_enemy:
        i.print_self()

def sort_atack():
    for i in range(0, len(list_enemy) - 1):
        for j in range(i + 1, len(list_enemy)):
            if list_enemy[i].atack < list_enemy[j].atack:
                list_enemy[i], list_enemy[j] = list_enemy[j], list_enemy[i]
    for i in list_enemy:
        i.print_self()
sort_atack()
# show_defense()
# del_atack()
