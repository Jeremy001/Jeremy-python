# -*- coding: utf-8 -*-

# numpy 数组
import numpy as np
a = np.array([1, 2, 3, 4, 0, -1, 5])
print(a)
print(a[:3])    # 切片，得到a的前三个元素
print(a.min())
a.sort()    # 对a排序（升序），相当于改变了a
print(a)
b = np.array([[1, 2, 3], [3, 4, 5]])    # 二维数组
print(b*b)

# scipy 矩阵
# 1.求解线性方程组
# 2x1 - x2^2 = 1
# x1^2 - x2 = 2
from scipy.optimize import fsolve
def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 - 1, x1**2 - x2 - 2]
result = fsolve(f, [1, 1])  # 输入初始值[1,1]并求解
print(result)
# 2.数值积分
from scipy import integrate     # 导入积分函数
def g(x):
    return (1 - x**2) ** 0.5
pi_2, err = integrate.quad(g, -1, 1)    # 积分结果和误差
print(pi_2*2)


# matplotlib
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1
plt.plot(x, y, label = '$\sin x + 1$', color = 'red', linewidth = 2)
plt.plot(x, z, 'b--', label = '$cos x^2 + 1$')
plt.xlabel("Time(s)")
plt.ylabel('Volt')
plt.title("A simple demo")
plt.ylim(0, 2.2)
plt.legend()
# plt.show()      # 显示图片


# pandas
# pandas主要用来做数据处理和探索
# pandas的两个主要数据结构是Series和DataFrame
import pandas as pd
# 创建一个序列Series
s = pd.Series([1, 2, 3], index = ['a', 'b', 'c'])
print(s)
# 创建一个DataFrame
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns = ['a', 'b', 'c'])
print(d)
# 把一个序列转换成DataFrame
d2 = pd.DataFrame(s)
print(d2)

# 默认预览前5行数据
d.head()
# 修改参数，预览前3行记录
d.head(n = 3)

# 读取文件，目录中最好不要有中文
# 读取Excel文件
d3 = pd.read_excel('E:/python/Jeremy-python/python_for_data_analysis_zhangliangjun/test_data.xlsx')
print(d3)
d4 = pd.read_csv('E:/python/Jeremy-python/python_for_data_analysis_zhangliangjun/test_data.csv', encoding = 'utf-8')
print(d4)


# statsmodels
# statsmodels主要用来做统计分析，和pandas结合做数据挖掘
from statsmodels.tsa.stattools import adfuller as ADF
import numpy as np
print(ADF(np.random.rand(100)))


# scikit-learn
# 机器学习包

# 线性回归模型
from sklearn.linear_model import LinearRegression
model = LinearRegression()
print(model)

# SVM模型
# 导入数据集
from sklearn import datasets
# 导入iris数据集
iris = datasets.load_iris()
# 查看iris数据集的大小
print(iris.data.shape)
# 导入SVM模型
from sklearn import svm
# 建立线性SVM分类器
clf = svm.LinearSVC()
# 用iris数据集训练分类器
clf.fit(iris.data, iris.target)
# 查看训练好的模型的参数
print(clf.coef_)
# 用分类器对新数据进行预测
print(clf.predict([[5.0, 3.6, 1.3, 0.25]]))


# keras
# 人工神经网络，深度学习


# gensim
# 主题模型
























