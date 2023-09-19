import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决坐标轴刻度负号乱码
plt.rcParams['axes.unicode_minus'] = False

# 解决中文乱码
mpl.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif'] = ['Simhei']

x = np.random.normal(loc=10000, scale=3000, size=10000)
bins = range(0, 20000, 500)

plt.hist(x, bins=bins, histtype='bar', color='b')

plt.xlabel('居民可支配收入')
plt.ylabel('人数')

plt.show()
