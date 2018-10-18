# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:31:32 2018
@author: Administrator
"""

import numpy as np
from numpy.linalg import *

print (np.eye(3))


def main():
    lst = [[1, 2, 3], [4, 5, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    # dtype定义array中的数据类型
    np_lst = np.array(lst, dtype=np.float)
    print(np_lst.shape)  # 矩阵形状
    print(np_lst.ndim)  # 矩阵行数
    print(np_lst.dtype)  # 矩阵数据类型
    print (np_lst.itemsize)  # 每个元素的字节大小  float是64位，占8 个字节所以是8
    print(np_lst.size)  # 所有字节
    # numpy  array
    print(np.zeros([2, 4]))
    print(np.ones([2, 3]))
    # 0~1均匀分布随机数
    print(np.random.rand(2, 4))
    print(np.random.rand())
    # 随机整数
    print(np.random.randint(1, 10, 3))
    # 标准正太分布随机数
    print(np.random.randn(2, 4))
    # 生成指定随机数
    print(np.random.choice([1, 2, 4]))
    # beta分布随机数
    print (np.random.beta(1, 10, 10))
    # 等差数列,arange算前不算后
    print(np.arange(1, 11).reshape([2, 5]))
    # 对数列进行计算
    lst1 = np.arange(1, 11).reshape([2, 5])
    print (np.exp(lst1))
    print(np.exp2(lst1))
    print (np.sin(lst1))
    print (np.log(lst1))
    print (np.sqrt(lst1))
    # axis
    lst2 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                     [[2, 2, 3, 4], [5, 6, 7, 8]],
                     [[3, 2, 3, 4], [5, 6, 7, 8]]])
    print(np.sum(lst2, axis=0))  # axis=0表示最外层的数据进行计算
    print(np.sum(lst2, axis=1))  # axis=1表示对倒数第二层的数据进行计算
    print(np.sum(lst2, axis=2))

    # linear
    lst3 = np.array([[1, 2], [3, 4]])
    # 矩阵的逆
    print(inv(lst3))
    # 转置
    print(lst3.transpose())
    # 行列式
    print (det(lst3))
    # 特征值
    print (eig(lst3))
    # 解方程
    y = np.array([[5.], [7.]])
    print (solve(lst3, y))

    if __name__ == '__main__':
        main()

# matplot;iv
