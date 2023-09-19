import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# %matplotlib inline
plt.style.use('ggplot')   # 修改绘图风格 R语言绘图库的风格

columns = ['user_id', 'order_dt', 'order_products', 'order_amount']
df = pd.read_table(r'D:\BaiduNetdiskDownload\3、用户消费行为数据分析\1-项目介绍,需求分析\资料\CDNOW_master.txt',names=columns, sep='\s+')  # \s是指空格，加个+代表任意数量的空格
# df  69659 rows × 4 columns

# df.head()
df['order_date'] = pd.to_datetime(df['order_dt'], format='%Y%m%d')

# df.head()

# df['month'] = df[''].astype('datetime64[M]')

# df['month'] = df['order_date'].index.year

# df['month'] = df.index.year

# 数据透视表
# index相当于groupby  values：取出来数据列  aggfunc：key值必须存在于values列中，并且必须跟随有效的聚合函数
rfm = df.pivot_table(index='user_id',
                     values=['order_products', 'order_amount', 'order_date'],
                     aggfunc={
                         'order_date': 'max',  # 最后一次购买时间
                         'order_amount': 'sum',  # 消费总金额
                         'order_products': 'sum'  # 购买产品的总数量
                     })

rfm.head()
rfm.rename(columns={'order_products': 'F', 'order_amount': 'M'}, inplace=True)

# rfm[['R', 'F', 'M']].apply(lambda x: x-x.mean())
rfm.groupby(by='label')
for label,grouped in rfm.groupby(by='label'):
    print(label,grouped)
rfm.groupby(by='label')
for label, grouped in rfm.groupby(by='label'):
    # print(label,grouped)
    x = grouped['F']
    y = grouped['R']
    plt.scatter(x,y,label=label)
plt.legend()    # 显示图例
plt.xlabel('F')
plt.ylabel('R')

privated_counts = df.pivot_table(
    index='user_id',
    columns='month',
    values='order_dt',
    aggfunc='count'
)

plt.legend()

