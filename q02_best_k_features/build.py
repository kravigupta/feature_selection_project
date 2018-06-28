# %load q02_best_k_features/build.py
# Default imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression
import operator

# Write your solution here:
def percentile_k_features(df, k=20):
    X = df.drop(['SalePrice'], axis=1)
    y = df['SalePrice']
    select_p = SelectPercentile(f_regression, percentile=k)
    select_p.fit(X,y)
    select_p.scores_
    d = dict()
    for n,s in zip(X.columns,select_p.scores_):
        d[n] = s    
    sorted_data = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    features = list()
    features = sorted_data[:7]
    features = [f for (f,v) in features]
    print(features)
    return features
percentile_k_features(data)

