from Person_message.Views.Add_View import Add_Views
from Person_message.Views.Delete_View import Delete_Views
from Person_message.Views.Find_View import Find_Views
from Person_message.Views.Modify_View import Modify_Views
from Person_message.Views.Show_View import Show_Views


class Message_Views:
    """
        （2）需要实现的功能
            1)	新增信息产业发展数据条目。
            2)	查找数据（可按地区、年份、指标名称等查找）。
            3)	修改数据条目（先查找，再修改。若当前条件查找出多个记录，则提示用户增加查询条件继续查找，直到确定唯一记录后再修改）。
            4)	删除数据条目（请参考上面修改的处理）。
            5)	显示信息产业发展数据列表。
    """

    def __init__(self):
        self.function_list = Message_Views.__read_configuration_file()
        self.length = len(self.function_list)

    @staticmethod
    def __read_configuration_file():
        list_func = []
        with open("config.txt", "r", encoding="utf-8") as f:
            text = f.readline()
            while text:
                str_text = text.split("-")
                list_func.append((str_text[0], str_text[1], str_text[2]))
                text = f.readline()
        return list_func

    def show_home_age(self):
        print("""
*************************************
*   欢迎光临&伟大信息产业发展统计系统  *
        """)
        for item in self.function_list:
            print('\t' + item[0], item[1])
        print("\t" + str(self.length + 1) + ".", "退出程序！")
        print("""
*************************************
        """)
        while True:
            n = self.__show_home_input(self.function_list)
            if n == -1:
                break

    def __show_home_input(self, list_func):
        n = input("请输入您要进入的功能:")
        try:
            if int(n) == self.length + 1:
                print("正在为您退出程序,欢迎下次光临 ^-^")
                return -1
            elif int(n) <= self.length:
                eval(list_func[int(n) - 1][2]).show_function()
        except:
            print("输入错误,请重新输入！")
