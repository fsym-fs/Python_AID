"""
Test09
    八大行星
        1.创建列表,存储行星("金星","地球","火星","木星","土星","天王星")
        2.在第一个位置插入"水星"
        3.在末尾追加"海王星"
        4.打印太阳到地球之间的行星(打印前两个行星)
        5.打印从地球以后的行星(一行一个)
        6.倒序打印所有行星
"""
planet = ["金星","地球","火星","木星","土星","天王星"]
planet.insert(0,"水星")
print(planet)
planet.append("海王星")
# planet.insert(-1,"海王星")
print(planet)
print(planet[:2])
for i in range(3,len(planet),1):
    print(planet[i])
for i in range(len(planet)-1,-1,-1):
    print(planet[i])
