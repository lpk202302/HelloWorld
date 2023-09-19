import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

# import pandas_profiling as pp

# df = pd.read_excel(r'D:\pycharm\Code\20230418\student-score.xlsx', index_col=0)

df = pd.read_excel(r'D:\pycharm\Code\20230418\test-score.xlsx', index_col=0)

print(df)

df.loc['1','语文'] = 100

print(df)

df.insert()

df = pd.concat([df, pd.DataFrame(columns=['年龄11'])])
