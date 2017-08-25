# -*- coding: utf-8 -*-

# sklearn中的数据集有以下这些 ===================================
# 1.自带的小型数据集（较小）
#     sklearn.datasets.load_<name>
# 2.可在线下载的数据集（较大）
#     sklearn.datasets.fetch_<name>
# 3.计算机生成的数据集
#     sklearn.datasets.make_<name>
# 4.svmlight / libsvm格式的数据集
#     sklearn.datasets.load_svmlight_file(...)
# 5.从mldata在线下载获取数据集
#     sklearn.datasets.fetch_mldata(...)

# 1.自带的小型数据集（较小） ===================================

# 手写数字数据集 load_digits()  用于多分类任务
from sklearn.datasets import load_digits
digits = load_digits()
# digits也是一个Bunch类型的数据集
print(type(digits))
print(digits.keys())
print(digits.data.shape)
# (1797, 64)
print(digits.images.shape)
# 可以发现：data.shape中的特征变量数 = images中的二维特征之积
# (1797, 8, 8)
print(digits.target.shape)
print(digits.data[:10,])
print(digits.target[:10])
print(digits.target_names)
print(digits.DESCR)
print(digits.images)

import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[2])
plt.show()

fig = plt.figure(figsize = (6, 6))      # 设置画布尺寸
fig.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1, hspace = 0.05, wspace = 0.05)

# 绘制数字
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks = [], yticks = [])
    ax.imshow(digits.images[i], cmap = plt.cm.binary, interpolation = 'nearest')
    ax.text(0, 7, str(digits.target[i]))
plt.show()


# 乳腺癌数据集 load_breast_cancer
# 用于二分类，良性 VS 恶性
from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
print(breast_cancer.keys())
print(breast_cancer.DESCR)


# 糖尿病数据集 load_diabetes()
# 回归分析
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
print(diabetes.keys())
print(diabetes.DESCR)


# 波士顿房价数据集 load_boston()
# 经典的用于回归分析的数据集
from sklearn.datasets import load_boston
boston = load_boston()
print(boston.DESCR)


# 体能训练数据集 load_linnerud


# 4.svmlight / libsvm格式的数据集 =================================
#     sklearn.datasets.load_svmlight_file(...)
# 每个样本的存放格式是：
# <label> <feature-id>:<feature-value> <feature-id>:<feature-value> <feature-id>:<feature-value> ...
# 这种格式比较适合存放稀疏矩阵
from sklearn.datasets import load_svmlight_file
X_train, y_train = load_svmlight_file('/path/to/train_data.csv')
# 注意以上的路径只是举例而已


