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
l=pd.Series([1,2,3,4,5,6,7,78,5,42])
print type(s)
print l
#创建日期
dates=pd.date_range('20170301',periods=8)#开始日期，持续天数
date=pd.date_range('20181101',periods=5)
#创建dataframe
df=pd.DataFrame(np.random.rand(8,5),index=dates,columns=list('ABCDE'))#数据8行5列0~1的随机数，行标题，列标题
print(df)
#创建dataframe方式2
df3=pd.DataFrame({'A':1,'B':pd.Timestamp('20170301'),'C':pd.Series(1,index=list(range(4)),dtype='float32'),\
                 'D':np.array([3]*4,dtype='float32'),'E':pd.Categorical(['police','student','teacher','doctor'])})

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
print (df[:3])#索引行
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

#set
sl=pd.Series(list(range(10,18)),index=pd.date_range("20170301",periods=8))
df['F']=sl
print(df)
df.at[dates[0],'A']=0#at表示行列定位
df.iat[1,1]=1#iat表示坐标定位
print df
df.loc[:,'D']=np.array([4]*len(df))#选择多行多列
print df
print len(df)
df2=df.copy()
df2[df2>0]=-df2
print df2
