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
#dandas基础模块应用
s1=pd.Series{}