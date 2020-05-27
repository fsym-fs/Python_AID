"""
    dataframe
"""
import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)
# 通过列表添加数据
data = ['张三', '李四', '哈哈聪', '翔儿子']
df = pd.DataFrame(data)
print(df)
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'], index=['s01', 's02', 's03'])
print(df)
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

# 从字典来创建DataFrame
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
print(df['Age'])
print(df)
data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)
print('*' * 50)
# print(df[0])
print('=' * 50)
print(df.axes)
# print(df.index[1])
print(df[df.columns[:2]])

# 列添加
df['four'] = pd.Series([90, 80, 70, ], index=['b', 'c', 'd'])
# df['four'] = pd.Series([1,2])
# df['four'] = [1,2,3,4]
# df['four'] = [1,2]
# print(df)
# # del
# df.pop('one')
# del(df['four'])
# df.drop('one',axis=1)
print(df)

# 行访问
print('-' * 50)
print(df.loc['a'])
# (1,-2,3)(-1,-5,-3)
# -1+10+-9
# 只有切片才可以当做行
print(df[0:1])

# df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
# df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])
#
# df = df.append(df2)
# print(df)
df = df.append(df)
print(df)
df.index = np.arange(8)
print(df)

# 值修改
# 列访问行
# df['Name'][0] = 'Tom'
print(df.loc[2:2])
