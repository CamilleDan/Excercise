# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:26:10 2018

@author: Administrator
"""
#excercise1
list1=[1,2,3,4]
for i in list1:
    for j in list1:
        for k in list1:
            if i!=j and j!=k and i!=k:
                print ('%d%d%d')%(i,j,k)

#excercise 2
#使用数轴
i=int(input('请输入净利润：'))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx]*rat[idx])
        print (i-arr[idx]*rat[idx])
        i=arr[idx]
print r

#excercise 3



#excercise 4




