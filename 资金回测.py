# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:06:22 2019

@author: Administrator
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_finance as mpf
import datetime
from matplotlib.pylab import date2num
import talib
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
df = pd.read_csv("F:/shuju/123456.csv",engine='python',sep=",")

print(df)


closedata=df["净值"]
datadate=df["时间"]
df["时间"] = pd.to_datetime(df["时间"])
df.set_index("时间", inplace=True)
print(df)


plt.plot(df["净值"])
plt.ylim((0.6,1.5))
plt.show()
fig=plt.subplots(figsize=(8,4))
data=df["净值"]
index_j = np.argmax(np.maximum.accumulate(data) - data)  # 结束位置
print("最低点在：",index_j)
index_i = np.argmax(data[:index_j])  # 开始位置
print("最高点在：",index_i)
d = data[index_j] - data[index_i]  # 最大回撤
print("最大回撤为: %.2f %%"%(d*100))

# 绘制图像
plt.plot(data)
plt.plot([index_i, index_j], [data[index_i], data[index_j]], 'o', color="r", markersize=10)
plt.ylim((0.6,1.5))
plt.show()

