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
print(df.head(3))
print(df.tail(3))
print(df.index)
print(df.values)
print(df.T)
print(df.sort(columns = "C"))
print(df.sort_index())
