# -*- coding: utf-8 -*-

# load pacakges =============================================
import pandas as pd
import ggplot
from sklearn.datasets import load_iris 

df = pd.DataFrame({"x":[1,2,3,4], "y":[1,3,4,2]})
ggplot(aes(x="x", weight="y"), df) + geom_bar()

















