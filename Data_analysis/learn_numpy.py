# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

import numpy as np
#array接受一切为序列型的对象
data=[1,2,3,4,3,5,6]
array=np.array(data)
data1=[[1,2,3],[1,2,1]]
array1=np.array(data1)
#数组维度和数据类型属性
print array1
print array1.shape
print array1.dtype
print array1.ndim

#可指定长度和形状的全0全1数组
zeros=np.zeros((2,3))
ones=np.ones((3,3))
print zeros
print ones

#empty数组可以创建一个没有数值的空矩阵，但没有数值不等于数值取0，eye表示单位矩阵
emp=np.empty((3,4))
i=np.eye(3)
print emp
print i

#创建一个以另一个数组为参数，并根据其形状dtype创建的全1数组
one1=np.ones_like(array1)
zero1=np.zeros_like(array1)
print zero1
print one1

#arange是range函数的数组版
array2=np.arange(13)
print array2

#ndarray的数据类型
arr1=np.array([1,2,3],dtype='int32')
print arr1.dtype
arr1=arr1.astype('float32')#转换数据类型
print arr1.dtype

#熊浮点数类型换为整数类型时小数点后面的数会被截断
arr2=np.array([1.2,3.2,13.22,3.11],dtype='float64')
print arr2
arr2=arr2.astype('int64')
print arr2

#字符串里面全是数字则可以转换为数字类型
arr3=np.array(['1.2','3.2','1.1'],dtype='string_')
print arr3
arr3=arr3.astype('float')
print arr3
print arr3.dtype

#数组和标量之间的运算
arr4=np.array([[1,2,3],[1,2,3]])
print arr4+arr4
print arr4**2
print arr4/2.0
#不同大小的数组在一起运算叫广播

#基本的索引和切片
arr5=np.array(np.arange(10))
print arr5[5]
print arr5[2:4]
print arr5[-3:]

#二维数组的索引
arr6=np.array([[1,2,3],[2,3,4],[3,4,5]])
print arr6[1]
print arr6[0][1]

#三维数组
arr7=np.array([[[1,2,3],[2,3,4]],[[2,3,4],[3,4,5]]])
print arr7
print arr7[0]
print arr7[0][1]
old_values=arr7[0][1].copy()
arr7[0][1]=[1,1,1]
print arr7

#切片索引
print arr6[:2]
print arr6[:2,1:]
arr6[:1,:]=0
print arr6[0,:].shape
print arr6[:1,:].shape
print arr6

#布尔值逻辑判断和切片
names=np.array(['bob','joe','will','joe','joe','bob','will'])
data=np.random.randn(7,4)
print names
print data

print names=='bob'
print data[names=='bob']

mark=(names=='bob')|(names=='will')
print data[mark]

data[data<0]=0
print data

data[names=='joe']=7
print data

#花式索引
arr8=np.empty((8,4))
for i in range(8):
    arr8[i]=i
print arr8
print arr8[[1,2,4,5]]
print arr8[[-1,-2,-5,-3]]
print arr8[[2,1,3]][:,[2,3,1]]
print arr8[np.ix_([1,2,1],[1,1,1])]#将两个以为整数数组转换为一个方形区域

#转置和轴对换
array3=np.arange(15).reshape(3,5)
print array3
print array3.T
array4=np.random.randn(6,3)#规定行列的标准正太随机数
ji=np.dot(array4,array4.T)#计算矩阵的內积
print ji

#通用的元素级数组函数
x=np.random.rand(10)
y=np.random.rand(10)

print np.sqrt(x)
print np.maximum(x,y)#两个数列对比提取每个元素的最大值
print np.modf((x+2.2))
print (x+2)**2
print np.log2(y)
print np.exp(x)
y=y.astype('float32')
print np.isnan(y)
