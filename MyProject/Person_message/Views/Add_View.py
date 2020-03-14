from Person_message.Views.Function_View import Function_Views
from Person_message.Controls.Add_control import Add_controls

class Add_Views(Function_Views):
    """
        新增信息产业发展数据条目
        信息产业发展数据是由多条数据记录构成，其信息包括：
            地区、年份、指标名称、计量单位、指标数量等。
                其中，地区包括：全国34个省、直辖市、自治区和港澳台；
                指标名称包括：固定电话用户数、移动电话用户数、互联网用户数、
                通信固定资产投入、通信业收入、信息服务收入、信息产品收入等。
    """
    def show_function(self):
        super().show_function()
    def add_message(self):
        print("输入您要添加的数据:")
        n1 = input("输入地区:")
        n2 = input("输入年份:")
        n3 = input("输入指标名称:")
        n4 = input("输入计量单位:")
        n5 = input("输入指标数量:")

