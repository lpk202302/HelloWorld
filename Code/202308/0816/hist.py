import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决坐标轴刻度负号乱码
plt.rcParams['axes.unicode_minus'] = False

# 解决中文乱码
mpl.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif'] = ['Simhei']

cityA = np.random.normal(loc=10000, scale=3000, size=10000)
cityB = np.random.normal(loc=8000, scale=1000, size=8000)
x = (cityA, cityB)
labels = ['A市', 'B市']
bins = range(0, 20000, 500)

plt.hist(x, bins=bins,histtype='bar', label=labels, stacked=True)

plt.xlabel('A市和B市居民人均收入')
plt.ylabel('人数')

plt.legend(loc='upper right')

plt.show()
