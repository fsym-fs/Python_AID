"""
    继承:
        创建一个父类--汽车类
                        品牌,价格
        一个子类--电动车类
                    电瓶容量,充电功率
"""


class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


class Electric_car(Car):
    def __init__(self, brand, price, capacity, charging_power):
        super().__init__(brand, price)
        self.capacity = capacity
        self.charging_power = charging_power



c = Car("吉利", 150000)
print(c.brand, c.price)
ec = Electric_car("艾玛", 1220, 10000, 1000)
print(ec.brand, ec.price, ec.capacity, ec.charging_power)
