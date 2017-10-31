# -*- coding: utf-8 -*-

# read json data ================================================
import json
path = 'pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
print(type(path))
print(type(records))
print(records[0])
print(records[0]['tz'])
# 获取每条记录的时区（并不是每条记录都有时区）
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])
# 对时区计数
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts
counts = get_counts2(time_zones)
print(counts['America/New_York'])
print(len(time_zones))
# 出现次数最多的前10个时区
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))

# DataFrame ===================================================
import pandas as pd
import numpy as np
frame = pd.DataFrame(records)
print(type(frame))
print(frame.head())
# TOP10
print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])
# 先处理缺失值
clean_tz = frame['tz'].fillna("Missing")
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print('-------------------------------')
print(tz_counts[:10])
# 绘图
tz_counts[:10].plot(kind = 'barh', rot = 0)


# 根据空格分割字段，并取分割后的第一个
results = pd.Series([x.split()[0] for x in frame.a.dropna()])
# 前5条有浏览器信息的记录
print(results[:5])
# 用得最多的浏览器TOP10
print(results.value_counts()[:10])




















