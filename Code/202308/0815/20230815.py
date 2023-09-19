import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决坐标轴刻度负号乱码
plt.rcParams['axes.unicode_minus'] = False

# 解决中文乱码
mpl.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif'] = ['Simhei']

# 创建一个图形
fig = plt.figure()

x = np.linspace(0.05, 20, 2000)
y = np.sin(x)

# 调用画图函数画图
#  参数说明：
#     x：x轴上面的值
#     y：y轴上面的值
#     ls：折线图的线条风格（linestyle）
#     lw：折线图的宽度风格（linewiight）
#     label：标记图形内容的标签文本
#     color：颜色
plt.plot(x, y, ls="-", lw=2, label="plot figure", color="r")

# 将标签展示出来  上面那个label的值
plt.legend()

plt.show()

fig.savefig('fig.png')
