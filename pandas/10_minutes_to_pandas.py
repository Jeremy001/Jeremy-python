# -*- coding: utf-8 -*-

# load packages =======================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('2017-01-01', periods = 6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4),
                  index = dates,
                  columns = list('ABCD'))
print(df)

df2 = pd.DataFrame({'A' : 1,
                   'B' : pd.Timestamp('20170103'),
                   'C' : pd.Series(1, index = list(range(4)), dtype = 'float32')，
                   'D' : np.array([3] * 4, dtype = 'int32'),
                   'E' })

print(df2)

















