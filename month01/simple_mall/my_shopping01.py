# # 简单商城
class Shopping_Models:
    def __init__(self, name, price, number, id):
        self.name = name
        self.price = price
        self.number = number
        self.id = id


class Mall_function:
    """
        生成商城的功能
    """
    shopping_mall = [
        Shopping_Models("屠龙刀", 10000, 55, 101),
        Shopping_Models("倚天剑", 10000, 45, 102),
        Shopping_Models("九阴白骨爪", 8000, 65, 103),
        Shopping_Models("九阳神功", 9000, 95, 104),
        Shopping_Models("降龙十八掌", 8000, 35, 105),
        Shopping_Models("乾坤大挪移", 10000, 25, 106),
    ]

    def __init__(self, f_name, f_id):
        self.f_name = f_name
        self.f_id = f_id

    def generate_function(self):
        pass


class Show_Mall_function_Controlles(Mall_function):
    def __init__(self, f_name, f_id):
        super().__init__(f_name, f_id)

    def generate_function(self):
        super().generate_function()
        self.show_all_goods()

    def show_all_goods(self):
        for good in Mall_function.shopping_mall:
            print("编号：%d,名称：%s,单价：%d,库存:%d." % (good.id, good.name, good.price, good.number))


class Show_Cart_function_Controlles(Mall_function):

    def __init__(self, f_name, f_id):
        super().__init__(f_name, f_id)
        self.cart = []
        self.total_price=0

    def generate_function(self):
        super().generate_function()
        self.show_shopping_cart()

    def show_shopping_cart(self):
        print("进入购物车成功!")
        for item in self.cart:
            for good in Mall_function.shopping_mall:
                if good.id == item.id:
                    print("商品编号:%d,商品:%s,单价:%d,数量:%d." % (good.id, good.name, good.price, item.number))
                    self.total_price += good.price * item.number

class Generate_Mall_function_Controlles:
    """
        功能生成器:生成商城的功能
    """

    def __init__(self):
        self.f_obj = []
        self.fun_list = self.read_configuration()
        self.generate()

    def read_configuration(self):
        return [
            (1, "展示商品", 'Show_Mall_function_Controlles("展示商品",1)'),
            (2, "进入购物车", 'Show_Cart_function_Controlles("进入购物车",2)'),
            (3, "展示商品", 'Show_Mall_function_Controlles("展示商品",3)'),
            (4, "进入购物车", 'Show_Cart_function_Controlles("进入购物车",4)'),
        ]

    def generate(self):
        for fun in self.fun_list:
            self.f_obj.append(
                (fun[0], fun[1], eval(fun[2]))
            )

    def show(self):
        for i in self.f_obj:
            print("\t", end="")
            print(i[0], i[1], sep=":")

    def in_function(self, n):
        self.f_obj[int(n) - 1][2].generate_function()


class User_Shopping_Views:
    def __init__(self):
        self.__controls = Generate_Mall_function_Controlles()
        self.__function_number = len(self.__controls.f_obj) + 1

    def main(self):
        while True:
            self.__show_home_page()
            if self.__user_input() == 0:
                break

    def __show_home_page(self):
        print("""
   欢迎光临-浮生@商城
*********************
        """)

    def __user_input(self):
        self.__controls.show()
        print("\t", end="")
        print(self.__function_number, "退出程序!", sep=":")
        print("""
*********************
        """)
        item = input("请输入您向进入的功能:")
        if int(item) < len(self.__controls.f_obj) + 1:
            self.__controls.in_function(item)
        elif int(item) == self.__function_number:
            print("欢迎下次光临,浮生@商城随时为您服务! ^_^")
            return 0
        else:
            print("输入错误!")


A = User_Shopping_Views()
A.main()
