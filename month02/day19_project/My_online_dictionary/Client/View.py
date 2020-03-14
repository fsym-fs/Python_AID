from Client.Controls import Client_Controls


class Client_View:

    def __init__(self):
        # 存放函数id和对应方法
        self.first_function_dict = {
            '1': self.__login_view,
            '2': self.__register_view,
            '3': self.__exit_view
        }
        self.second_function_dict = {
            '1': self.__find_word_view,
            '2': self.__find_history_view,
            '3': self.__logout_view
        }
        self.client = Client_Controls()

    # 进入相应界面视图
    def __into_page(self, func_page, fun_dict):
        while True:
            func_page()
            item = self.__use_input(fun_dict)
            a = fun_dict[item]()
            if a == "out":
                break

    # 进入程序
    def show(self):
        self.__into_page(self.__show_first_page, self.first_function_dict)

    # 展示初始界面
    def __show_first_page(self):
        print("***欢迎使用随风潜相思@Online_Dictionary***")
        print("*            1.登录                    *")
        print("*            2.注册                    *")
        print("*            3.退出                    *")
        print("****************************************")

    # 登录后进入功能界面
    def __show_second_page(self):
        print("***欢迎使用随风潜相思@Online_Dictionary***")
        print("*            1.查找单词                 *")
        print("*            2.查看历史                 *")
        print("*            3.注销账号                 *")
        print("****************************************")

    # 用户功能选择视图
    def __use_input(self, func_dict):
        while True:
            item = input("输入您要进入的功能:")
            if item not in func_dict:
                print("输入错误,请重新输入!")
            else:
                break
        return item

    # 登录视图
    def __login_view(self):
        if self.client.login():
            print("登录成功!")
            self.__into_page(self.__show_second_page, self.second_function_dict)
        else:
            print("登录失败!")

    # 注册视图
    def __register_view(self):
        if self.client.register():
            print("注册成功!")
        else:
            print("注册失败!")

    # 退出视图
    def __exit_view(self):
        if self.client.do_exit():
            exit("即将退出!")
        else:
            print("退出失败!")

    # 查找单词视图
    def __find_word_view(self):
        while True:
            if self.client.find_words() == "out":
                break

    # 查看历史记录视图
    def __find_history_view(self):
        self.client.history()

    # 注销视图
    def __logout_view(self):
        return "out"
