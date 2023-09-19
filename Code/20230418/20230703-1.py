# 相关系数
import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import numpy as np
import pandas as pd
import seaborn as sns
import scipy as stats
from statsmodels.formula.api import ols

data_raw = pd.read_excel('D:\CDA\LR_practice.xlsx')


# 删除无用的三列
data_raw.drop(['id','Acc','edad2'],axis=1,inplace=True)

# 删除重复值
data_raw.drop_duplicates(inplace=True)

# 删除缺失值
# 查看缺失值
data_raw.isnull().mean()
data_raw.isnull().sum()

# 填补缺失值
data_raw['avg_exp'].mean()
data_raw['avg_exp'].fillna(data_raw['avg_exp'].mean())

data_raw.isnull().mean()
# 赋值
data_raw['avg_exp'] = data_raw['avg_exp'].fillna(data_raw['avg_exp'].mean())

data_raw.isnull().mean()

# 转换为list
label = data_raw['edu_class'].unique().tolist()

label

label.index('中学')

# 对原数据进行编码  apply,label  都是内置函数
data_raw['edu_class'] = data_raw['edu_class'].apply(lambda x: label.index(x))

data_raw['edu_class'].value_counts()

# dist_avg_income
sns.boxplot(data=data_raw['dist_avg_income'])

# 标准化数据，三倍标准差
# 没查到，报错  zscore
#z = stats.zscore(data_raw['Age'])
#z

# 寻找异常数据的索引
#z[(z>2)|(z<-3)]

# 查看异常数据的值
data_raw['Age'].iloc[40]

# 对这个异常数据进行填补 1，均值
data_raw['Age'].mean()
# 要在删除999之后在求均值

data_raw['Age'].drop(index=40).mean()

# 哑变量转换
pd.get_dummies(data=data_raw['edu_class'], prefix='edu', drop_first='True')

dummy = pd.get_dummies(data=data_raw['edu_class'], prefix='edu', drop_first='True')

# 把哑变量合并到原数据
data = pd.concat([data_raw,dummy],axis=1)
data.head()

# 相关系数
data.corr()

# 分类变量
data.corr(method='kendall')

# 散点图
# avg_exp和Income
plt.scatter(data['Income'], data['avg_exp'])
plt.show()

# 建立回归模型
data.columns

ols()
