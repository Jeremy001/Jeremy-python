# -*- coding: utf-8 -*-


from io import StringIO
import pandas as pd
import numpy as np


csv_data = pd.read_csv('./csv_data.csv')

csv_data.is_null.sum()









