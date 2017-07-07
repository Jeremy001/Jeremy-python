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





















