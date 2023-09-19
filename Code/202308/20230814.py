import pandas as pd
import numpy as np

# dates = pd.date_range('20200315', periods = 5)
# df = pd.DataFrame(np.arange(20).reshape((5,4)), index = dates, columns = ['A','B','C','D'])
# print(df)
#
# df.loc['20200315','C'] = 20200315
#
# print(df)

df1 = pd.DataFrame(data=[['apple', '10'],
                         ['banana', '20']],
                   columns=['fruits','num'],
                   index=[1,2])

print(df1)

df1.drop()
