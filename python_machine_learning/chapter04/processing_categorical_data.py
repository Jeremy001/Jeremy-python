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


# 对离散特征进行独热编码(哑变量)

# 以下编码有问题
# 因为转换之后，颜色本来的无序性被转换成有序了，0,1,2
X = df[['color',  'size', 'price']].values
# color_le = LabelEncoder()
# X[:, 0] = color_le.fit_transform(X[:, 0])
# print(X)
print(X)

# 独热编码 -- 哑特征
# 什么是哑特征呢？举例来说，对于‘颜色’这一特征中的‘蓝色’，我们将其编码为[蓝色=1，绿色=0，红色=0]，同理，对于‘绿色’，我们将其编码为[蓝色=0，绿色=1，红色=0]，特点就是向量只有一个1，其余均为0，故称之为one-hot。

from sklearn.preprocessing import OneHotEncoder
# ohe = OneHotEncoder(categorical_features = [0])
# ohe.fit_transform(X).toarray()
# print('-------------------------')
# print(X)

# 还可以用pandas的get_dummies来创建哑变量
X2 = pd.get_dummies(df[['price', 'color', 'size']])
print(X2)

























