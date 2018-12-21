# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
l=range(1,5)
s=[]
for i in l:
    for j in l:
        for k in l:
            if i!=j and i!=k and k!=j:
                d=i,j,k#会形成一个元素为tuple的list
                s.append(d)#把元素添加到空列表里

print s
print len(s)
print type(s[0])

l=['1','2','3','4']
s=[]
for i in l:
    for j in l:
        for k in l:
            if i!=j and i!=k and k!=j:
                d=i+j+k#‘+’是字符串连接符，若用于整数则会变为加运算
                s.append(d)#会形成一个元素为str的list
print s
print len(s)
print type(s[0])

#exercise 2

i=int(input("请输入利润："))
arr=[1000000,600000,400000,200000,100000,0]
rate=[0.01,0.015,0.03,0.05,0.075,0.1]
bonus=0
for idx in range(0,6):
    if i>arr[idx]:
        bonus+=(i-arr[idx])*rate[idx]
        print (i-arr[idx])*rate[idx]
        i=arr[idx]
print '总利润为：%d'%bonus
