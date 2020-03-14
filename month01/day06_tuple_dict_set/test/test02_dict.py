"""
Test02_dict
    1.在终端中循环录入商品的信息(名称,单价)
      如果名称为空,停止录入
      打印所有商品信息(一行一个)
      格式为:...的价格是...
      如果录入的是游戏机,则打印其价格
"""
print("录入商品的名称和价格")
goods = {}
while True:
    name = input("名称:")
    if name == "":
        break
    else:
        pice = input("价格:")
        goods[name] = pice

for key, value in goods.items():
    print("%s的价格是%s元" % (key, value))
try:
    print(goods["游戏机"])
except:
    pass
