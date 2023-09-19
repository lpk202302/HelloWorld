import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决坐标轴刻度负号乱码
plt.rcParams['axes.unicode_minus'] = False

# 解决中文乱码
mpl.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif'] = ['Simhei']

x = [1, 2, 3, 4, 5]
y = np.random.randint(1, 100, 5)
z = ['小红', '小李', '小张', '小白', '小孙']

plt.ylabel('成绩')
plt.xlabel('学员')

plt.barh(x, y, align='center', color='r', tick_label=z)

plt.show()
