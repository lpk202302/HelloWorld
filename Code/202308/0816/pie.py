import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决坐标轴刻度负号乱码
plt.rcParams['axes.unicode_minus'] = False

# 解决中文乱码
mpl.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif'] = ['Simhei']

percent = '0.4', '0.3', '0.2', '0.1'
explode = 0, 0, 0, 0.5
types = '优', '良', '中', '差'
aotu

plt.pie(percent, explode=explode, labels=types,)

plt.show()