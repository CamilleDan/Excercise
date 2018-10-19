# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
#数值计算的库SciPy
#积分
import numpy as np
from scipy.integrate import quad,dblquad,nquad
#一元积分
print (quad(lambda  x:np.exp(-x),0,np.inf))#函数，积分上下限
#二元积分
print (dblquad(lambda  t,x :np.exp(-x*t)/t**3,0,np.inf,lambda x:1,lambda x:np.inf))
#n元积分
def f(x,y):
    return x*y
def bound_y():
    return [0,0.5]
def bound_x(y):
    return [0,1-2*y]
print (nquad(f,[bound_x,bound_y]))

#optermiser
from scipy.optimize import minimize
def rosen(x):
    return  sum(100.0*(x[1:]-x[:-1]**2.0)+(1-x[:-1])**2.0)
x0=np.array([1.3,0.7,0.8,1.9,1.2])
res=minimize(rosen,x0,method='nelder-mead',options={'xtol':le-8,'disp':True})
def func(x):
    return (2*x[0]*x[1]+2*x[0]-x[0]**2-2*x[1]**2)
def func_deriv

