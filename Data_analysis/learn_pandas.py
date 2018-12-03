# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

import pandas as pd
import numpy as np

s=pd.Series([1,-2,3,4])
print s
s1=pd.Series([1,-2,3,4],index=['a','b','c','d'])
print s1
print s1.index
print s1.values
s1.index=['a','e','r','t']
print s1.index

s.name='text'#对象名称
s.index.name='text'#索引名称
print s

data1={'a':1,'b':'','c':'4a','d':'p'}#用字典创建dataframe
s2=pd.Series(data1)
print s2
print s2.isnull()#判断是否有缺失值
index=['a','b','c','e']
s2=pd.Series(data1,index=index)#会根据索引自动匹配data1里面的元素，不存在的index现实为Nan
print s2.notnull()#判断是否有缺失值

#Dataaframe
data={'id':[1,2,3,4],'name':['bob','joe','will','lisa'],'states':['LA','NY','California','NY']}#字典类型的Series创建df
df1=pd.DataFrame({'id':[1,2,3,4],'name':['bob','joe','will','lisa'],'states':['LA','NY','California','NY']},index=[1,2,3,4])
df2=pd.DataFrame(data,columns=['id','name','states','debt'])#对已有数据进行创建新的df时，df会根据column自动匹配存在的数据，不存在的column则显示为nan
print df2
print df1['states']
print df1.ix[2]#索引index
df2['debt']=[1200,1300,2200,1500]#新增column
df2['debt']=np.arange(4)
val=pd.Series([1,2.2,3],index=[0,2,1])
df2['est']=val#以Series的方式添加df的column
print df2
del df2['est']#删除df的column
print df2
#注意，index不可修改！！！！！！！！

#嵌套式字典
zi={'gz':{'2001':12,'2002':13},'xj':{'2001':12,'2002':22}}
df3=pd.DataFrame(zi).T#内层的key会自动变为index
df3.name='enviroment'
df3.index.name='city'
df3.columns.name='year'
print df3
print df3.index
print df3.values

#索引对象
index=df3.index
print index
#index[0]='bj'#index对象是不可被修改的！
print 'gz' in index
print 'bj' in index
print index

#Index对象的append方法
ind1=df3.T.index
ind2=pd.Index(['2003','2004'])
ind=pd.Index.append(ind1,ind2)
print ind
#计算index对象的差集
ind_diff=pd.Index.difference(ind,ind1)
print ind_diff
#intersection交集，union并集，isin判断是否包含，delete删除索引i处的元素病得到新的index
#drop删除传入的值，insert插入，unique计算唯一值得数组

#reindex前向填充
obj=pd.Series(['red','blue','yellow'],index=[0,2,4])
obj=obj.reindex(range(6),method='ffill')
print obj

#drop方法的使用
df4=pd.DataFrame(np.arange(16).reshape(4,4),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
df4.drop('Ohio')
df4.drop(['one','two'],axis=1)

arr=np.arange(12.).reshape(3,4)
print arr-arr[0]#

frame=pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('abc'))
series=frame.loc[0,['a','b','c']]
print series
print frame-series

frame1=pd.DataFrame(np.random.randn(4,4),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
print frame1
print np.abs(frame1)

f=lambda x:x.max()-x.min()
print frame1.apply(f,axis=0)
print frame1.apply(f,axis=1)
print frame1
print frame1.sum(axis=1)#求和
print frame1.mean(axis=0)#求均值

print frame1.sort_index(axis=1)#根据索引的大小排序
print frame1.sort_index(axis=0,ascending=False)#根据索引的大小排序,降序

series1=pd.Series([4.,9.2,np.nan,7,np.nan,3])
print series1.sort_values(ascending=False)#按照数值排序，逆序，所有的nan会被放到最后

print frame1.sort_values(by=['one','two'])#按照某一列或几列的值排序

series2=pd.Series([2,4,2,6,7,1,0,1])
series2.rank(method='first')#按照出现的顺序排序,可以降序
series2.rank()#普通排序，两个相同的值会并列同级
frame1.rank(method='first',axis=0)#匹配行
frame1.rank(method='first',axis=1)#匹配列
frame1.rank(method='average')#匹配列

frame2=pd.DataFrame(np.arange(16).reshape(4,4),index=['a','a','b','b'],columns=list('1234'))
print frame2.loc['a','1']#当index重复索引行是会显示所有相同index的行
print frame2.index#可检查是否有重复index

frame3=pd.DataFrame([[2,np.nan],[3,4],[2.5,1]])
frame3.sum(axis=1,skipna=True)
frame3.idxmax(axis=1)#按列执行，找最大值的索引
frame3.cumsum(axis=0)#按行执行，累计求和
frame3.cumprod(axis=0)#按行执行，累计求积
frame3.cummax(axis=0)#按行执行，累计找最大值
frame1.describe()#五数汇总