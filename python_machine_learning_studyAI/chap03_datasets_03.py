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

# 2.可在线下载的数据集（较大） ==================================
#     sklearn.datasets.fetch_<name>

# 20类新闻文本数据集

# fetch_20newsgroups(): 返回一个原始的文本列表，
# 可以输入到文本特征提取器sklearn.feature_extraction.text.CountVectorizer中进一步处理得到特征向量

# fetch_20newsgroups_vectorized(): 返回可以直接使用的特征，无需再提取

# 数据集存放的默认位置
from sklearn.datasets import get_data_home
print(get_data_home())


from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset = 'train')
# 可用的参数：
# data_home:指定下载的数据集存放的路径
# subset:指定下载训练集/测试集/全部
# shuffle:是否把数据集打乱
# categories:下载哪些新闻类别？可以传入一个list
# 。。。

from pprint import pprint

print(type(newsgroups_train))
print(newsgroups_train.keys())
print(newsgroups_train.filenames)
print(newsgroups_train.target_names)
print(newsgroups_train.data[:2])

pprint(list(newsgroups_train.target_names))

# 真正的数据存放在filenames和target中
# filenames里面是新闻文本你文件名
# target里面是新闻类别的标签

print(newsgroups_train.filenames.shape)
print(newsgroups_train.target.shape)
print(newsgroups_train.target[:10])


# 下载指定新闻分类的数据
cats = ['alt.atheism', 'comp.graphics']
newsgroups_train_2 = fetch_20newsgroups(subset = 'train',
                                        categories = cats)
print(newsgroups_train_2.filenames.shape)
print(newsgroups_train_2.target.shape)
print(newsgroups_train_2.target[:10])


# 提取文本特征向量
from sklearn.feature_extraction.text import TfidfVectorizer
cats = ['alt.atheism', 'comp.graphics']
newsgroups_train = fetch_20newsgroups(subset = 'train',
                                      categories = cats)
vct = TfidfVectorizer()
vectors = vct.fit_transform(newsgroups_train.data)
print(vectors.shape)


# 可以直接用fetch_20newsgroups_vectorized来提取已经向量化的新闻文本数据集
from sklearn.datasets import fetch_20newsgroups_vectorized
newsgroups_train = fetch_20newsgroups_vectorized()
print(newsgroups_train.keys())





# 野外人脸数据集 fetch_lfw_people and fetch_lfw_pairs



















