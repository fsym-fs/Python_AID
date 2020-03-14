"""
Test01
    获取商品价格
    获取购买数量
    获取支付金额
    支付 - 价格*数量
    显示应该找回?元或者钱不够
"""
# 获取支付金额
pay = input("Input  pay:\n")
# 获取商品价格
price = input("Input price:\n")
# 获取购买数量
number = input("Input number:\n")
# 显示应该找回?元
change = int(pay) - int(price) * int(number)
"""
Test01
    获取商品价格
    获取购买数量
    获取支付金额
    支付 - 价格*数量
    显示应该找回?元或者钱不够
"""
# 获取支付金额
pay = input("Input  pay:\n")
# 获取商品价格
price = input("Input price:\n")
# 获取购买数量
number = input("Input number:\n")
# 显示应该找回?元
change = int(pay) - int(price) * int(number)
if change > 0:
    print("Your change :   " + str(change))
    
"""
Test01
    获取商品价格
    获取购买数量
    获取支付金额
    支付 - 价格*数量
    显示应该找回?元或者钱不够
"""
# 获取支付金额
pay = input("Input  pay:\n")
# 获取商品价格
price = input("Input price:\n")
# 获取购买数量
number = input("Input number:\n")
# 显示应该找回?元
change = int(pay) - int(price) * int(number)
if change > 0:
    print("Your change :   " + str(change) + " RMB")
elif change == 0:
    print("您的支付正好!")
else:
    print("钱不够")