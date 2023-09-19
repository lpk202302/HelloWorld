import os
import numpy as np
import pandas as pd
import matplotlib as plt
import warnings


# 忽略报错
warnings.filterwarnings('ignore')

# 当前工作路径
os.chdir(r"D:\CDA\data\week5\2022-03-05")

df = pd.read_csv(r'0116-聚类分析\cities_10.csv', encoding='gbk')

df.head()

# 第一列area删除
model_data = df.loc[:, 'X1':]

model_data

# 计算距离，主成分分析之前 都要进行标准化
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler_model = scaler.fit_transform(model_data)

from sklearn.decomposition import PCA

# n_components主成分的个数  方差的累计占比起码占80%  开始可以设置为大一点，后面慢慢调整
pca = PCA(n_components=2)
pca_model_data = pca.fit(scaler_model)

# 主成分可解释的变异
pca1 = pca.explained_variance_
# 主成分可解释的累计占比
pca2 = pca.explained_variance_ratio_



# 因子分析

