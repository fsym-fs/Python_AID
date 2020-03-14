"""
    Enclosing 外部嵌套作用域:函数嵌套
    nonlocal
    闭包/封闭并保存内存空间
        保存内部函数栈帧的内存空间
    价值:
        逻辑连续
    装饰器:

"""
"""
    在不改变函数(进入后台,删除订单)的定义与调用基础上,为其增加新功能(验证权限)
"""


def verif_permissions(func):
    def wapper(*args,**kwargs):
        print("验证权限")
        return func(*args,**kwargs)

    return wapper


@verif_permissions
def enter_background(login_id, pwd):
    print(login_id, "加入后台")


@verif_permissions
def delete_order(id):
    print("删除%d订单" % id)


enter_background("zz@qq.com", "1234")
delete_order(10010)
