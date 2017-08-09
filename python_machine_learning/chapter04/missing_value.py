# -*- coding: utf-8 -*-

# load packages ===================================

from io import StringIO
import pandas as pd
import numpy as np

# dataset ========================================
# csv_data = '''A, B, C, d
#                         1.0, 2.0, 3.0, 4.0
#                         5.0, 6.0, , 8.0
#                         0.0, 11.0, 12.0,'''
# csv_data = unicode(csv_data)
# df = pd.read_csv(stringIO(csv_data))
# df

csv_data = pd.read_csv('./csv_data.csv')
print(csv_data)

# 处理缺失值 =======================================

# 汇总各变量的缺失值样本数
csv_data.isnull().sum()
# print(csv_data.isnull().sum())

# dataframe中的数据
csv_data.values

# 丢弃缺失值 =======================================
# 1.丢弃含缺失值的样本行
csv_data.dropna()
# print(csv_data.dropna())

# 2.丢弃含缺失值的变量
csv_data.dropna(axis = 1)
print(csv_data.dropna(axis = 1))

# 3.丢弃每个变量均为缺失值的样本行
csv_data.dropna(how = 'all')
print(csv_data.dropna(how = 'all'))

# 4.丢弃非缺失值变量数少于n的样本行
csv_data.dropna(thresh = 4)
print(csv_data.dropna(thresh = 4))

# 5.丢弃制定列含有缺失值的样本行
csv_data.dropna(subset = ['C'])
print(csv_data.dropna(subset = ['C']))

# 缺失值插补 =======================================
# 1.用变量的平均值插补
from sklearn.preprocessing import Imputer
imr = Imputer(missing_values = "NaN", strategy = 'mean', axis = 0)
imr = imr.fit(csv_data)

imputed_data = imr.transform(csv_data.values)

print(csv_data)
print('----------------------------')
print(imputed_data)





