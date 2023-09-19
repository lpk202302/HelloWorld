import unittest
import pandas as pd
import matplotlib as plt

# class MyTestCase(unittest.TestCase):
#    def test_something(self):
#        self.assertEqual(True, False)  # add assertion here


# if __name__ == '__main__':
#    unittest.main()

# data_raw = pd.read_excel('D:\CDA\data\week4\2022-2-26\第四周第2天-数据采集与处理、数据管理、多维分析\第4周-周日-3数据采集与处理 3 数据预处理基础\donations.csv')

data_raw = pd.read_csv("D:\date\donations.csv")

data_raw.head(5)

plt.hist(comp[''])