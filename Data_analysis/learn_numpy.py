# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

import numpy as np
import matplotlib.pyplot as plt

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

#数组进行数据处理
point=np.arange(-5,5,0.01)
ys,xs=np.meshgrid(point,point)
print ys

# z=np.sqrt(xs**2+ys**2)
# print z
# plt.imshow(z)
# plt.colorbar()

#将条件逻辑表述转化为数组运算
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result=np.where(cond,xarr,yarr)#条件，满足时替换为，不满足时替换为
print result
#where方法
arr=np.random.randn(4,4)
print arr
arr=np.where(arr>0,2,-2)
print arr

#统计方法
array5=np.arange(12).reshape(3,4)
print array5
print array5.mean()#所有元素求平均
print array5.mean(axis=0)#axis=0表示按列计算，1表示按行计算
print array5.sum()#所有元素求和
print array5.cumsum(1)#按列累计求和
print array5.cumprod(0)#按行累计求积

#布尔数组方法
ran=np.random.randn(100)
print (ran>0).sum()#正值的数量
ran1=np.array([1,0,0,0])
print ran1.any()#所有非0元素会被当成True；只能判断数值类型不能判断复合型数组

#排序
arr3=np.random.randn(8)
arr3.sort()
print arr3
arr3=np.random.randn(4,4)
arr3.sort(axis=1)#按行升序排序
print arr3
#排序计算分位数
long_arr=np.array([1,2,3,4,5,5,5,6,7,3,4,5,6,8,9,10,1,12,1,3,2,2,2,3,3,3,1,1,1,1])
long_arr.sort()
percent25=long_arr[int(0.25*len(long_arr))]
print percent25

#数组的集合运算
name1=['bob','joe','bob','will','joe','will']
name2=['john','amy','bob','joe','kate','john','kate']
np.unique(name1)
np.intersect1d(name1,name2)#返回公共元素
np.union1d(name1,name2)#返回并集
np.in1d(name1,name2)#返回x是否包含y的布尔数组
np.setdiff1d(name1,name2)#返回数组的差
np.setxor1d(name1,name2)#返回数组的对称差

np.save('long_arr.npy',long_arr)#以二进制格式将数组保存到磁盘，后缀名为npy
np.load('long_arr.npy')
np.savez('arraies.npz',a=long_arr,b=arr3)#将多个数组保存到一个压缩文件中后缀名为npz
arr6=np.load('arraies.npz')#以字典的 形式加载
print arr6['a']
print arr6['b']

#矩阵运算
x1=np.array([[1,2],[3,2]])
y1=np.array([1,1])
prod=np.dot(x1,y1)#矩阵乘法
print prod
from numpy.linalg import qr,inv
mat=x1.T.dot(x1)#矩阵的转置乘矩阵
inv_mat=inv(mat)#矩阵的逆
q,r=qr(mat)#矩阵的qr分解
print r
print inv_mat
xx1=inv_mat.dot(mat)
print xx1

