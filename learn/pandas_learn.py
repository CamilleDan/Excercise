# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
# pandas
# seriers and dataframe

import pandas as pd
from pylab import *

# 创建series
s = pd.Series([i * 2 for i in range(1, 11)])  # series 是pandas的基本数据结构
l = pd.Series([1, 2, 3, 4, 5, 6, 7, 78, 5, 42])
print type(s)
print l
# 创建日期
dates = pd.date_range('20170301', periods=8)  # 开始日期，持续天数
date = pd.date_range('20181101', periods=5)
# 创建dataframe
df = pd.DataFrame(np.random.rand(8, 5), index=dates, columns=list('ABCDE'))  # 数据8行5列0~1的随机数，行标题，列标题
print(df)
# 创建dataframe方式2
df3 = pd.DataFrame({'A': 1, 'B': pd.Timestamp('20170301'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), \
                    'D': np.array([3] * 4, dtype='float32'),
                    'E': pd.Categorical(['police', 'student', 'teacher', 'doctor'])})

print (df.head(3))  # 前3行
print df.tail(3)  # 后3行
print df.index  # 显示索引
print df.values  # 显示数值
print df.T  # 转置
print df.sort_index(axis=1, ascending=False)  # 降序排列
print df.describe()  # 五数描述
# print (df.sort(columns='A'))不存在的语句

# select by id切片
print (df['A'])  # 按照列名索引
print (type(df['A']))
print (df[:3])  # 索引行
# 切片索引
print (df['20170301':'20170304'])  # 索引index
print (df.loc[dates[0]])  # 表位置
print (df.loc['20170301':'20170304', ['D', 'B']])  # 同时锁定行列行，列
print (df.at[dates[0], 'C'])  # at表定位
# iat，iloc
print (df.iloc[1:3, 2:4])  # 行，列
print (df.iloc[1, 4])
print (df.iat[2, 4])
# 逻辑判断进行切片
print(df[df.B > 0][df.A < 0])
print(df[df > 0])
print (df[df['E'].isin([1, 2])])
# set
sl = pd.Series(list(range(10, 18)), index=pd.date_range("20170301", periods=8))
df['F'] = sl
print(df)
df.at[dates[0], 'A'] = 0  # at表示行列定位
df.iat[1, 1] = 1.235453  # iat表示坐标定位
df.loc[:, 'D'] = np.array([4] * len(df))  # 选择多行多列
print df
print len(df)
df2 = df.copy()
df2[df2 > 0] = -df2
print df2
# 缺失值处理
df1 = df.reindex(index=dates[:4], columns=list('ABCD') + ['G'])
df1.loc[dates[0]:dates[1], ['G']] = 1
print df1
# print df1.dropna()
print df1.fillna(value=2.0937674)

# 数据整合、统计
print(df.mean(), df.var())
s = pd.Series([1, 2, -4, np.nan, 5, 7, 3, 5], index=dates)
print s
print s.shift(2)  # 下移两位
print s.diff()  # 一节差分
print s.value_counts()  # 绘制直方图方便
print df.apply(np.cumsum)  # 列累加
print df.apply(lambda x: x.max() - x.min())  # 每列的极差
# 表格拼接和类sql的操作
pieces = [df[:3], df[-3:]]
print pd.concat(pieces)
left = pd.DataFrame([['x', 1], ['y', 2]], columns=['key', 'value'])
right = pd.DataFrame([['x', 3], ['z', 4]], columns=['key', 'value'])
print left
print right
print pd.merge(right, left, on='key', how='outer')
df4 = pd.DataFrame({'A': ['a', 'b', 'c', 'b'], 'B': list(range(4))})
print df4.groupby('A').sum()

# 时间序列绘图、文件操作
t_exam = pd.date_range('20181101', periods=10, freq='S')
print t_exam
s2 = pd.Series(np.random.randn(1000), index=pd.date_range('20181115', periods=1000))  # randn标准正态分布
s2 = s2.cumsum()
s2.plot()
# show()

# file
df5 = pd.read_csv('E://demo/test.csv')
df6 = pd.read_excel('E://demo/test.xlsx')
print df5
print df6
