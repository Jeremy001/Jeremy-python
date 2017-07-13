# encoding = utf-8

import numpy as np
import pandas as pd

# 认识Series 和 DataFrame
# Series
s = pd.Series([i * 2 for i in range(1, 11)])
print(s)
print(type(s))
# DataFrame
dates = pd.date_range("20170301", periods = 8)
df = pd.DataFrame(np.random.randn(8, 5),
                  index = dates,
                  columns = list("ABCDE"))
print(df)
print(type(df))

# df2 = pd.DataFrame({"A":1,
#                    "B":pd.Timestamp("20170301"),
#                    "C":pd.Series(1, index = list(range(4)), dtype = "float32"),
#                    "D":np.array([3] * 4, dtype = "float32"),
#                    "E":pd.Categorical(["police", "student", "teacher", "doctor"])})
# print(df2)

# pandas基本操作
# 前3条记录
print(df.head(3))
# 后三条记录
print(df.tail(3))
# 数据框的索引列
print(df.index)
# 数据框的所有数据
print(df.values)
# 数据框转置
print(df.T)
# 下面的sort怎么有错呢？
# print(df.sort(columns = "C"))
# 把字段降序排列
print(df.sort_index(axis = 1, ascending = False))
# 数据框的基本描述
print(df.describe())


# select 切片
# A列
print(df["A"])
# 数据类型是Series
print(type(df["A"]))
# 前三条记录
print(df[:3])
# 数据类型是DataFrame
print(type(df[:3]))
# 前四条记录，根据index列来查询
print(df["20170301":"20170304"])
# loc第一条记录
print(df.loc[dates[0]])
print(type(df.loc[dates[0]]))
# 前三条记录，从0开始，0代表第一条记录，不包括最后一个
print(df.loc[dates[0:3]])
# 前三条记录的BCD三个字段
print(df.loc["20170301":"20170304", ["B", "C", "D"]])
# at，特定数据点
print(df.at[dates[0], 'C'])

# 根据下标进行切片
# iloc[n1:n2, n3:n4]
# 从0开始，0表示第一个记录，不包括最后一个
# DataFrame
print(df.iloc[1:3, 2:4])
# 数据点
print(df.iloc[1, 4])
print(df.iat[1, 4])

# 根据条件进行切片
# B>0 & A<0
print(df[df.B>0][df.A<0])
# DataFrame中满足条件的所有数据点
print(df[df>0])
# E的取值范围
print(df[df["E"].isin([1, 2])])

# 为DataFrame添加数据列
s1 = pd.Series(list(range(10, 18)), index = pd.date_range("20170301", periods = 8))
df["F"] = s1
print(df)

# 修改DataFrame的数据点或数据列
df.iat[0, 0] = 0
df.at[dates[1], "B"] = 1
df.loc[:, "D"] = np.array([4] * len(df))
print(df)

# 复制DataFrame
df2 = df.copy()
print(df2)
# 把df2中的正数全部转换成负数
df2[df2>0] = -df2
print(df2)


# 缺失值处理
# 准备数据
df1 = df.reindex(index = dates[:4], columns = list("ABCD")+["G"])
df1.loc[dates[0]:dates[1], "G"] = 1
print(df1)
# 缺失值处理方法1：直接丢弃
print(df1.dropna())
# 缺失值处理方法2：插值
# 插值方法1：固定值
print(df1.fillna(value = 2))
# 插值方法2：按一定规则插值


# 统计statistic
print(df.mean())
print(df.var())
s = pd.Series([1, 2, 4, np.nan, 5, 7, 9, 10], index = dates)
print(s)
# 把数据序列往后移2个位置
print(s.shift(2))
# 计算环比差异，可以设置阶数，即当前记录与前几个记录的值进行比较
print(s.diff())
print(s.diff(2))
# 计算各个value出现的次数
print(s.value_counts())
# 应用函数
print(df.apply(np.cumsum))
print(df.apply(lambda x:x.max() - x.min()))


# 拼接DataFrame，类似数据库的union
pieces = [df[:3], df[-3:]]
print(pd.concat(pieces))

# merge DataFrame，类似数据库的join
left = pd.DataFrame({"key":["x", "y"],
                    "value":[1, 2]})
right = pd.DataFrame({"key":["z", "y"],
                    "value":[4, 3]})
print("LEFT:", left)
print("RIGHT:", right)
print(pd.merge(left, right, on = "key", how = "left"))
print(pd.merge(left, right, on = "key", how = "right"))
print(pd.merge(left, right, on = "key", how = "inner"))
print(pd.merge(left, right, on = "key", how = "outer"))


# groupby
df3 = pd.DataFrame({"A":["a", "b", "c", "b"],
                   "B":list(range(4))})
print(df3.groupby("A").sum())


# reshape
import datetime
df4 = pd.DataFrame({"A":["one", "one", "two", "three"] * 6,
                   "B":["a", "b", "c"] * 8,
                   "C":["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
                   "D":np.random.randn(24),
                   "E":np.random.randn(24),
                   "F":[datetime.datetime(2017, i, 1) for i in range(1, 13)] +
                   [datetime.datetime(2017, i, 15) for i in range(1, 13)]})
# 透视表
print(pd.pivot_table(df4, values = "D", index = "A", columns = "C"))


# Time Series
# 创建时间序列，20个时间点，间隔为秒
t_exam1 = pd.date_range("20170301", periods = 20, freq = "S")
# 间隔为月
t_exam2 = pd.date_range("20170301", periods = 20, freq = "M")
print(t_exam1, t_exam2)


# Graph
ts = pd.Series(np.random.randn(1000), index = pd.date_range("2000-01-01", periods = 1000))
ts = ts.cumsum()
from pylab import *
ts.plot()
show()


# 文件操作

# 读入文件
df6 = pd.read_csv("./data/df.csv")
df7 = pd.read_excel("./data/df.xlsx", "sheet1")

# 写出文件
df.to_csv("./data/df.csv")
df.to_excel("./data/df.xlsx")
