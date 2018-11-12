# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

import numpy as np
import pandas as pd
#numpy 入门
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
b=a[-2:,1:3]
print a
print np.shape(a)
print b

c=a[np.arange(3),1]#索引里面有整数会对原元素造成降维
c=a[0:3,1:2]#这种写法不会造成降维
print c
print np.shape(c)

print a.dtype
a1=np.array([1.3,1.3])
print a1.dtype
b1=np.array(a1,dtype=np.int64)
print b1
#常用函数
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
#print a+b
print np.add(a,b)
print np.subtract(b,a)
print np.multiply(a,b)
print np.divide(b,a)
print np.sqrt(b)
print a.dot(b)#矩阵乘法==np.dot(a,b)
#常用函数
print np.sum(a)
print np.sum(a,axis=1)#对行操作，0表示对列操作
print np.mean(a,axis=0)#列平均数
print np.random.uniform(3,4)
print np.random.rand(5)#5个0~1之间的随机数
print np.tile(a,(2,3))#行重复两次列重复三次
#矩阵转置
print a
print a.T#矩阵转置
print a.transpose()

#广播
c=np.array([[1,2,3],
            [2,3,4],
            [12,33,12],
            [21,34,4]])
b=np.array([1,2,3])
for i in range(4):
    c[i,:]+=b
print c
b=np.tile(b,(4,1))
print c+b
b1=np.array([1,2,3])
print c+b1

#量化交易
#pandas基础模块应用Series
s=pd.Series([1,2,3,4,3],index=['a','b','c','d','e'])
print s
s1=pd.Series(['f',2,3.0,True,3],index=['a','b','c','d','e'])
print s1
s2=pd.Series([1.0,2,3.0,3.2,3],index=['a','b','c','d','e'])
print s2
s3=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
print s3
s4=pd.Series(np.array([1,2,3,4,5]))#Series对象只能是一维的
print s4
#使用字典创建series可以不写index，若写index则会根据index排序显示series，index无值显示NAN
s5=pd.Series({'A':1,'C':'T','B':True},index=['A','B','C'])
print s5
#数值长度小于index时数值会自动补齐index
s6=pd.Series(5.,index=['a','b','c'])
print s6
#series对象的访问
#s.values,s.index,索引，切片
s5=pd.Series({'A':1,'C':'T','B':True,'e':1.9},index=['A','B','C','e'])
print s5.values
print s5.index
print s5['A']
print s5[['A','B','C']]
print s5[:2]
print s5[3]
#Dataframe生成和访问方法
df1=pd.DataFrame({'a':[1.67,22,'a',True],'b':[1.73,22,'b',False]},
                 index=['height','age','id','is inland'])
print df1
#使用二维np.ndarray创建dataframe
#创建2行n列的0矩阵
data=np.zeros((2,),dtype=[('a','i4'),('b','f4'),('c','a10')])#dtype指定列名和数据类型
#替换0矩阵的值
data[:]=[(1,2,'hello'),(2,4,'python')]
#用ndarray创建Dataframe
df2=pd.DataFrame(data,index=['first','second'],columns=['a','c','b','d'])
print df2
#以列表形式的字典创建dataframe
df3=pd.DataFrame([{'a':1.0,'b':'r'},{'a':2.0,'b':'e','c':True}])
print df3
df3=pd.DataFrame([{'a':1.0,'b':'r'},{'a':2.0,'b':'e','c':True}])

#pandas基础模块应用ndarray

s=pd.Series([1.2,2.3,3,34],dtype='int8')
print s
#以ndarray数据类型创建Series
s1=pd.Series([1.23,'r',0.98,4,True],index=['a','b','c','d','e'])#数据，行名，数据类型
print s1
s2=pd.Series(np.random.rand(3),index=['i','d','f'])
print s2
#以字典创建Series
s3=pd.Series({'a':0,'b':'a','c':True},index=['s','a','b','c'])#若为字典制定index，则index会自动匹配字典的key，匹配不到的显示nan
print s3

#Series访问方法
#s.index,s.values，索引，切片
print s.values
print s1.index
print s1[['a','b']]
print s1[2:3]

#dataframe
df1=pd.DataFrame({'one':[1,2,3,4],'two':[1.2,3.4,2,2]},index=['l','a','b','c'])
print df1
#dataframe访问方法
#df.index,df.values,df.columns,df.loc,df.ix

#导入文件数据
csv1=pd.read_csv('c://',index_col=0,encoding='gb2312')#文件路径
#header=1表示行标题在第几行None表示文件没有列索引，names=range(2,8)，
#encoding=''