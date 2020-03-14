class Good:
    def __init__(self, mall_dict=None, goods_dict=None, cid=None, name=None, price=None):
        self.goods_dict = goods_dict
        self.mall_dict = mall_dict
        self.cid = cid
        self.name = name
        self.price = price

    def show_all_goods(self):
        for key, value in self.mall_dict.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
shang_pin_info = \
    {
        101: {"name": "屠龙刀", "price": 10000},
        102: {"name": "倚天剑", "price": 10000},
        103: {"name": "九阴白骨爪", "price": 8000},
        104: {"name": "九阳神功", "price": 9000},
        105: {"name": "降龙十八掌", "price": 8000},
        106: {"name": "乾坤大挪移", "price": 10000}
    }
a = Good(shang_pin_info)
a.show_all_goods()
