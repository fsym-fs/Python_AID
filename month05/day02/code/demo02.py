"""
CustomerSurvival.py 用户流失数据初步分析
"""
import numpy as np


# 加载数据 做初步分析
def read_csv():
    with open('CustomerSurvival.csv', 'r') as f:
        data = []
        for line in f.readlines():
            data.append(tuple(line[:-1].split(',')))
        # 把data装进ndarray 返回
    print(data)
    data = np.array(data, dtype={
        'names': ['index', 'pack_type', 'extra_time', 'extra_flow', 'pack_change',
                  'contract', 'asso_pur', 'group_user', 'use_month', 'loss'],
        'formats': ['i4', 'i4', 'f8', 'f8', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4']})
    return data


data = read_csv()
print(data['loss'])
# 统计有多少种套餐类型
types = set(data['pack_type'])
print('\n-------统计有多少种套餐类型----------')
print(types)

# 每种套餐类型的数据量占比
print('\n-------每种套餐类型的数据量占比----------')
for t in types:
    mask = data['pack_type']==t
    sub_data = data[mask] # 获取每一小组数据
    print(t, '类型的数据量占比：', len(sub_data) / len(data))
print("其中，流失用户占比：", len(sub_data[sub_data['loss']==1]) / len(sub_data),
'未流失用户占比：', len(sub_data[sub_data['loss']==0]) / len(sub_data))

print("结论：由上述数据可知，套餐越贵，越不易流失。")
