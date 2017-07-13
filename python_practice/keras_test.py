# encoding = utf-8

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

# 创建一个人工神经网络
from sklearn.datasets import load_iris
iris = load_iris()
print(iris["target"])
# 标签化，把target3个结果0/1/2分别转成100， 010， 001
from sklearn.preprocessing import LabelBinarizer
LabelBinarizer().fit_transform(iris["target"])
# 分割数据集，训练集和测试集
from sklearn.cross_validation import train_test_split
train_data, train_target, test_data, test_target = train_test_split(iris.data, iris.target, test_size = 0.2, random_state = 1)
# labels_train = LabelBinarizer().fit_transform(train_target)
# labels_test = LabelBinarizer().fit_transform(test_target)


# 构建模型
model = Sequential(
                   [
                        Dense(5, input_dim = 4),
                        Activation("relu"),
                        Dense(3),
                        Activation("sigmoid"),
                   ])

# 另一种构建模型的语法是：
# model = Sequential()
# model.add(Dense(5, input = 4))
# ...


# 优化器
sgd = SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)

model.compile(optimizer = sgd, loss = "categorical_crossentropy")
model.fit(train_data,train_target, nb_epoch = 200, batch_size = 40)
print(model.predict_classes(test_data))


# 把这次训练的参数保存下来
model.save_weights("./data/w")

# 加载现有的参数
model,load_weights("./data/w")















