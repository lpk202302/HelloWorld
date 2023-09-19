import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决坐标轴刻度负号乱码
plt.rcParams['axes.unicode_minus'] = False

# 解决中文乱码
mpl.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif'] = ['Simhei']

np.random.seed(10)

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, color='r', label='散点图')
plt.legend()

plt.show()
