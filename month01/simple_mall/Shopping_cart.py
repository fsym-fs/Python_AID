class Shopping_cart():
    def __init__(self, cart=[], cid=None):
        self.cart = cart

    def show_shopping_cart(self):
        print()
        # for item in self.cart:
        #     shang_pin = self.shang_pin_info[item["cid"]]
        #     print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
        #     self.total_price += shang_pin["price"] * item["count"]


my_cart = Shopping_cart()
my_cart.show_shopping_cart()
