# encoding = utf-8

# load packages ============================================
import numpy as np
import pandas as pd


# datasets ================================================
# 创建一个数据集，包含有序特征，无序特征，数值型和类别型变量
df = pd.DataFrame([['green', 'M', 10.1, 'class1'],
                                ['red', 'L', 13.5, 'class2'],
                                ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']

print(df)

# processing ==============================================

# 自定义映射函数，把有序型分类字符串转换成整型数值
size_mapping = {
    'XL':3,
    'L':2,
    'M':1
}
df['size'] = df['size'].map(size_mapping)
print(df)

# 把整型变量转换回原来的字符串：定义反映射字典
inv_size_mapping = {v:k for k, v in size_mapping.items()}
df['size'] = df['size'].map(inv_size_mapping)
print(df)


# 对类别进行编码
# 把类别字符串转换成整型数值
class_mapping = {label:idx for idx, label in enumerate(np.unique(df['classlabel']))}
print(class_mapping)
df['classlabel'] = df['classlabel'].map(class_mapping)
print(df)

# 把整型数值转换成类别字符串
inv_class_mapping = {v:k for k, v in class_mapping.items()}
df['classlabel'] = df['classlabel'].map(inv_class_mapping)
print(df)

# 用现有函数进行类别转换
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
y = class_le.fit_transform(df['classlabel'].values)
print(y)
df['classlabel'] = class_le.fit_transform(df['classlabel'].values)
print(df)
# 得到原始的字符串类型
print(class_le.inverse_transform(y))
df['classlabel'] = class_le.inverse_transform(df['classlabel'].values)
print(df)



























