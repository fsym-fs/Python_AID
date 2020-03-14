"""
test01
    1.["齐天大圣","猪八戒","唐三藏"]--->key:字符,value:字符长度
    2.["张无忌","赵敏","周芷若"] [101,102,103]-->{"张无忌":101..}
    3.将练习二的字典的键与值颠倒
    4.  骰子 1--6
        骰子 1--6
        骰子 1--6
        将三个骰子的组合数存入列表
"""
a = {'cid': 101, 'count': 1}
print(a['cid'])
# if 101 in a['cid'] :
#     print("44")
# print(a[1])
try:

    xyj = ["齐天大圣", "猪八戒", "唐三藏"]
    dict_xyj = {key: len(key) for key in xyj}
    print(dict_xyj)

    yttlj_name = ["张无忌", "赵敏", "周芷若"]
    yttlj_key = [101, 102, 103]
    yttlj_dict = {yttlj_name[i]: yttlj_key[i] for i in range(len(yttlj_name))}
    print(yttlj_dict)

    yttlj_dict2 = {values: key for key, values in yttlj_dict.items()}
    print(yttlj_dict2)
except:
    print("程序错误!")
