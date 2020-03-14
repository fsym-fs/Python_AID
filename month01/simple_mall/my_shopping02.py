# 简单商城
class Shopping_Models:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number


# class Shopping_cart_Models:
#     def __init__(self, name, price, number):
#         self.name = name
#         self.price = price
#         self.number = number


class Shopping_Views:
    def __init__(self):
        self.__controls = Shopping_Controllers()

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


class Shopping_Controllers:
    def __init__(self):
        self.shang_pin_info = {
            101: {"name": "屠龙刀", "price": 10000, "number": 55},
            102: {"name": "倚天剑", "price": 10000, "number": 45},
            103: {"name": "九阴白骨爪", "price": 8000, "number": 65},
            104: {"name": "九阳神功", "price": 9000, "number": 95},
            105: {"name": "降龙十八掌", "price": 8000, "number": 35},
            106: {"name": "乾坤大挪移", "price": 10000, "number": 25}
        }
        # self.shopping_cart = Shopping_cart_Models()
        self.cart = []
        self.total_price = 0

    def show_all_goods(self):
        for key, value in self.shang_pin_info.items():
            print("编号：%d,名称：%s,单价：%d,库存:%d." % (key, value["name"], value["price"], value["number"]))

    def find_goods(self, cid):
        if cid in self.shang_pin_info:
            return 1
        else:
            return 0

    def merge_goods(self, cid, count):
        if self.shang_pin_info[cid]["number"] >= count:
            for shop in self.cart:
                if cid == shop['cid']:
                    shop['count'] += count
                    self.shang_pin_info[cid]["number"] -= count  # 扣除商品的数量
                    return 1
            self.shang_pin_info[cid]["number"] -= count
            self.cart.append({"cid": cid, "count": count})
            return 1
        else:
            return 0

    def show_shopping_cart(self):
        for item in self.cart:
            shang_pin = self.shang_pin_info[item["cid"]]
            print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
            self.total_price += shang_pin["price"] * item["count"]

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


shopping = Shopping_Views()
shopping.main()
