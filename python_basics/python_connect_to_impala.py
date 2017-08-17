# -*- coding: utf-8 -*-

# load packages =====================================================
import numpy as np
import pandas as pd
from connect_impala_neo import connect_impala
from impala.util import as_pandas

# read data using sql ==================================================
cur = connect_impala()
cur.execute(
    'select order_id, order_sn, shipping_time, pay_time from jolly.who_order_info limit 10'
    )
df = as_pandas(cur)
print(df.head())


















