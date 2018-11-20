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

