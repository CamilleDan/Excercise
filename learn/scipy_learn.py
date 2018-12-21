# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
# 数值计算的库SciPy
# 积分
import numpy as np
from scipy.integrate import quad, dblquad, nquad
from pylab import *

# 一元积分
print (quad(lambda x: np.exp(-x), 0, np.inf))  # 函数，积分上下限
# 二元积分
print (dblquad(lambda t, x: np.exp(-x * t) / t ** 3, 0, np.inf, lambda x: 1, lambda x: np.inf))


# n元积分
def f(x, y):
    return x * y


def bound_y():
    return [0, 0.5]


def bound_x(y):
    return [0, 1 - 2 * y]


print (nquad(f, [bound_x, bound_y]))

# optermiser
# 求全局最小值
from scipy.optimize import minimize


# 创建目标函数
def rosen(x):
    return sum(100.0 * (x[1:] - x[:-1] ** 2.0) + (1 - x[:-1]) ** 2.0)


x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])  # 算法必须的数组
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})  # 计算最小值算法nelder-mead，xtrol精度，disp中间过程
print ('reson mini', res.x)  # 打印属性


# 求条件最小值
# 创建目标函数
def func(x):
    return -(2 * x[0] * x[1] + 2 * x[0] - x[0] ** 2 - 2 * x[1] ** 2)


def func_deriv(x):  # 原函数、目标函数相对于xy的偏导数
    dfdx0 = -(-2 * x[0] + 2 * x[1] + 2)
    dfdx1 = -(2 * x[0] - 4 * x[1])
    return np.array([dfdx0, dfdx1])


# 约束条件，
cons = (
{'type': 'eq', 'fun': lambda x: np.array([x[0] ** 3 - x[1]]), 'jac': lambda x: np.array([3.0 * (x[0] ** 2.0), -1.0])},
{'type': 'ineq', 'fun': lambda x: np.array([x[1] - 1]), 'jac': lambda x: np.array([1.0, 0.0])})  # 雅克比行列式
res = minimize(func, [-1.0, 1.0], jac=func_deriv, constraints=cons, method='SLSQP', options={'disp': True})  # cons约束条件
print ('RESTRICT:', res)
from scipy.optimize import root


def fun(x):
    return x + 2 * np.cos(x)


sol = root(fun, 0.1)
print ('toot:', sol.x, sol.fun)

# 插值
x = np.linspace(0, 1, 10)
y = np.sin(2 * np.pi * x)
from scipy.interpolate import interp1d

li = interp1d(x, y, kind='cubic')
x_new = np.linspace(0, 1, 50)
y_new = li(x_new)
figure()
plot(x, y, 'r')
plot(x_new, y_new, 'k')
show()
print (y_new)
# 线性计算、矩阵分解
from scipy import linalg as lg

arr = np.array([[1, 2], [3, 4]])
print ('drt:', lg.det(arr))  # 行列式
print('lnv:', lg.inv(arr))  # 逆矩阵
b = np.array([6, 14])
print('sol', lg.solve(arr, b))  # 求解矩阵
print('eig:', lg.eig(arr))  # 特征值
print('lu:', lg.lu(arr))  # lu分解
print('qr:', lg.qr(arr))  # qr分解
print('svd:', lg.svd(arr))  # svd分解
print('schur:', lg.qschur(arr))  # qschur分解
