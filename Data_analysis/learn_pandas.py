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