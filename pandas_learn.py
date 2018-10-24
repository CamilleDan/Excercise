# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
#pandas
#seriers and dataframe
import numpy as np
import pandas as pd
#创建series
s=pd.Series([i*2 for i in range(1,11)])#series 是pandas的基本数据结构
print type(s)
#创建日期
dates=pd.date_range('20170301',periods=8)#开始日期，持续天数
#创建dataframe
df=pd.DataFrame(np.random.rand(8,5),index=dates,columns=list('ABCDE'))#数据，行标题，列标题
print(df)
#创建dataframe方式2
# df1=pd.DataFrame({'A':1,'B':pd.Timestamp('20170301'),'C':pd.Series(1,index=list(range(4)),dtype='float32'),\
#                  'D':np.array([3]*4,dtype='float32'),'E':pd.Categorical(['police','student','teacher','doctor'])})
# print df1
print (df.head(3))#前3行
print df.tail(3)#后3行
print df.index#显示索引
print df.values#显示数值
print df.T#转置
print df.sort_index(axis=1,ascending=False)#降序排列
print df.describe()#五数描述
# print (df.sort(columns='A'))不存在的语句

#select by id
print (df['A'])#按照列名索引
print (type(df['A']))
print (df[:3])#索引列
#切片索引
print (df['20170301':'20170304'])
print (df.loc[dates[0]])#
print (df.loc['20170301':'20170304',['D','B']])#行，列
print (df.at[dates[0],'C'])

#select by index
print (df.iloc[1:3,2:4])#行，列
print (df.iloc[1,4])
print (df.iat[2,4])

print(df[df.B>0][df.A<0])
print (df[df>0])