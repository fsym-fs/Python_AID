# 简单商城
class Merchants_Views:
    pass


class Merchants_Controllers:
    pass


class Shopping_Models:
    def __init__(self, name, price, number, id):
        self.name = name
        self.price = price
        self.number = number
        self.id = id


class Shopping_cart_Models:
    def __init__(self, id, number):
        self.number = number
        self.id = id


class User_Shopping_Views:
    def __init__(self):
        self.__controls = User_Shopping_Controllers()

    def main(self):
        while True:
            self.__show_home_page()
            if self.__user_input() == 0:
                break

    def __show_home_page(self):
        print("""
    欢迎光临-浮生@商城
*************************
*   1 键  展示所有商品    *
  * 2 键  进入购物车    *
*   3 键  退出程序       *
*************************
                    """)

    def __user_input(self):
        item = input("请输入您向进入的功能:")
        if item == "1":
            self.__show_all()
            self.__show_buy()
            self.__input_buy()
        elif item == "2":
            self.__show_cart()
            if self.__controls.total_price == 0:
                pass
            else:
                self.__controls.paying()
        elif item == "3":
            print("欢迎下次光临,浮生@商城随时为您服务! ^_^")
            return 0
        else:
            print("很抱歉,您的输入错误,请重新输入!")

    def __show_all(self):
        self.__controls.show_all_goods()

    def __show_buy(self):
        print("""
    欢迎光临-浮生@商城
*************************
*   1 键  购买商品       *
  * 2 键  进入购物车    *
*   3 键  返回上一层     *
*************************
                            """)

    def __input_buy(self):
        item = input("请输入您向进入的功能:")
        if item == "1":
            self.__add_shoppings()
        elif item == "2":
            self.__show_cart()
            if self.__controls.total_price == 0:
                pass
            else:
                self.__controls.paying()
        elif item == "3":
            print("正在返回上一层,请您稍等片刻.... ^_^")
            return 0
        else:
            print("很抱歉,您的输入错误,请重新输入!")

    def __add_shoppings(self):
        while True:
            cid = int(input("请输入商品编号："))
            if self.__controls.find_goods(cid) == 1:
                break
            else:
                print("该商品不存在")
        count = int(input("请输入购买数量："))
        if self.__controls.merge_goods(cid, count) == 1:
            print("添加到购物车.")
        else:
            print("库存不足,很抱歉!")

    def __show_cart(self):
        self.__controls.show_shopping_cart()


class User_Shopping_Controllers:
    shopping_mall = [
        Shopping_Models("屠龙刀", 10000, 55, 101),
        Shopping_Models("倚天剑", 10000, 45, 102),
        Shopping_Models("九阴白骨爪", 8000, 65, 103),
        Shopping_Models("九阳神功", 9000, 95, 104),
        Shopping_Models("降龙十八掌", 8000, 35, 105),
        Shopping_Models("乾坤大挪移", 10000, 25, 106),
    ]

    def __init__(self):
        self.cart = []
        self.total_price = 0

    def show_all_goods(self):
        for good in User_Shopping_Controllers.shopping_mall:
            print("编号：%d,名称：%s,单价：%d,库存:%d." % (good.id, good.name, good.price, good.number))

    def find_goods(self, cid):
        for good in User_Shopping_Controllers.shopping_mall:
            if good.id == cid:
                return 1
        return 0

    def merge_goods(self, cid, count):
        for good in User_Shopping_Controllers.shopping_mall:
            if good.id == cid and good.number >= count:
                for shop in self.cart:
                    if cid == shop.id:
                        shop.number += count
                        good.number -= count
                        return 1
                good.number -= count
                self.cart.append(Shopping_cart_Models(cid, count))
                return 1
        else:
            return 0

    def show_shopping_cart(self):
        for item in self.cart:
            for good in User_Shopping_Controllers.shopping_mall:
                if good.id == item.id:
                    print("商品编号:%d,商品:%s,单价:%d,数量:%d." % (good.id, good.name, good.price, item.number))
                    self.total_price += good.price * item.number

    # 结算购物车
    def paying(self):
        while True:
            qian = float(input("总价%d元,请输入金额：" % self.total_price))
            if qian >= self.total_price:
                print("购买成功,找回：%d元." % (qian - self.total_price))
                self.cart.clear()
                self.total_price = 0
                break
            else:
                print("金额不足.")


shopping = User_Shopping_Views()
shopping.main()
