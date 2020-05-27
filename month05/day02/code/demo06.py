"""
        复合索引
"""
import numpy as np
import pandas as pd

# random.normal() 返回一组服从正态分布随机数,shap:(6.3)
# 均值８５，。标准差是３（６，３）是维度(六行三列)
data = np.floor(np.random.normal(85, 3, (6, 3)))
df = pd.DataFrame(data)
print('-' * 50)
print(df)
index = [('classA', 'F'), ('classA', 'M'), ('classB', 'F'), ('classB', 'M'), ('classC', 'F'), ('classC', 'M')]
# 将原索引改为复合索引
df.index = pd.MultiIndex.from_tuples(index)
columns = [('Age', '20+'), ('Age', '30+'), ('Age', '40+')]
# 将列索引改为复合索引
df.columns = pd.MultiIndex.from_tuples(columns)
print(df)

# 通过复合索引访问元素
print('*' * 50)
print(df.loc['classA', 'F']['Age'])
print('-'*50)
print(df['Age','30+'])
