"""
作业
1. 三合一
2. 当天练习独立完成
3. 画出下列代码内存图
    name01  = "孙悟空"
    list_names = ["八戒"]
    tuple_names = ("唐僧",name01,list_names)
    name01 = "齐天大圣"
    tuple_names[2][0] = "猪八戒"
    print(tuple_names)
4. 定义数据结构，存储以下数据
    (1) "qtx"喜欢"编码","看书","跑步","音乐"
        "lzmly"喜欢"刷抖音","看电影","吃"
         ...
        -- 打印qtx的所有喜好(一行一个)
        -- 打印所有人的名称(一行一个)
        -- 打印所有人的喜好(一行一个)
    (2)
        "北京"
            "景区" -- "故宫","天安门","天坛"
            "美食" -- "豆汁","焦圈","烤鸭"
        "天津"
            "景区" -- "天津之眼","瓷房子"
            "美食" -- "狗不理包子","大麻花","煎饼"
        -- 打印北京的所有美食(一行一个)
        -- 打印天津的所有景区(一行一个)
        -- 打印所有城市(一行一个)
        -- 打印所有景区(一行一个)
        -- 给北京增加一个"美食"炸酱面
5. (扩展)计算字符中每个字符出现的数量
    "abacdce"
        a出现的次数是2次
        b出现的次数是1次
        c出现的次数是2次
        d出现的次数是1次
        e出现的次数是1次
"""


class homework:
    #1
    def people(self, person):
        try:
            for i in person["qtx"]:
                print(i)
            for i in person.keys():
                print(i)
            for i in person.values():
                print(i)
        except:
            print("程序错误!")

    #2
    def city(self, citys):
        try:
            for i in citys["北京"]["foods"]:
                print(i)
            for i in citys["天津"]["views"]:
                print(i)
            for i in citys.keys():
                print(i)
            for i in citys.values():
                for j in i["views"]:
                    print(j)
            citys["北京"]["foods"].append("炸酱面")
            print(citys)
        except:
            print("程序错误!")

    #3
    def account(self, str_word):
        try:
            num = {}
            for i in set(str_word):
                num[i] = 0
                for j in str_word:
                    if i == j:
                        num[i] += 1
            print(num)
        except:
            print("程序错误!")


hw = homework()
person = {"qtx": ["编码", "看书", "跑步", "音乐"], "lzmly": ["刷抖音", "看电影", "吃"]}
citys = {
    "北京": {"views": ["故宫", "天安门", "天坛"], "foods": ["豆汁", "焦圈", "烤鸭"]},
    "天津": {"views": ["天津之眼", "瓷房子"], "foods": ["狗不理包子", "大麻花", "煎饼"]}
}
str_word = "abacdce"
try:
    hw.people(person)
    hw.city(citys)
    hw.account(str_word)
except:
    print("程序错误!")

# # 4
# def people():
#     person = {"qtx": ["编码", "看书", "跑步", "音乐"], "lzmly": ["刷抖音", "看电影", "吃"]}
#     for i in person["qtx"]:
#         print(i)
#     for i in person.keys():
#         print(i)
#     for i in person.values():
#         print(i)
#
#
# people()
#
# # 5
# citys = \
#     {
#         "北京":
#             {
#                 "views":
#                     [
#                         "故宫", "天安门", "天坛"
#                     ],
#                 "foods":
#                     [
#                         "豆汁", "焦圈", "烤鸭"
#                     ]
#             },
#         "天津":
#             {
#                 "views":
#                     [
#                         "天津之眼", "瓷房子"
#                     ],
#                 "foods":
#                     [
#                         "狗不理包子", "大麻花", "煎饼"
#                     ]
#             }
#     }
# """
#         -- 打印北京的所有美食(一行一个)
#         -- 打印天津的所有景区(一行一个)
#         -- 打印所有城市(一行一个)
#         -- 打印所有景区(一行一个)
#         -- 给北京增加一个"美食"炸酱面
# """
#
#
# def city():
#     for i in citys["北京"]["foods"]:
#         print(i)
#     for i in citys["天津"]["views"]:
#         print(i)
#     for i in citys.keys():
#         print(i)
#     for i in citys.values():
#         for j in i["views"]:
#             print(j)
#     citys["北京"]["foods"].append("炸酱面")
#
#
# city()
#
#
# # 6
# def account():
#     str_word = "abacdce"
#     num = {}
#     for i in set(str_word):
#         num[i] = 0
#         for j in str_word:
#             if i == j:
#                 num[i] += 1
#     print(num)
#
# account()
