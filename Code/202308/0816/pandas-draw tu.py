import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决坐标轴刻度负号乱码
plt.rcParams['axes.unicode_minus'] = False

# 解决中文乱码
mpl.rcParams['font.family']='sans-serif'
plt.rcParams['font.sans-serif'] = ['Simhei']

df = pd.read_excel(r'D:\pycharm\Code\20230418\test-score.xlsx', index_col=0)
