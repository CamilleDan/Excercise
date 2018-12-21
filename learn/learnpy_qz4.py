# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
fn = 'e:\demo\\f.txt'
F = open(fn, 'r').readlines()  # 打开文件（文件名，打开方式）通过读取每一行字符创将其放入F

x = 0
z = 0

for i in F:
    x += 1
    if 'python' in i.lower():
        z += 1
        y = i
        print (y.decode('gbk'))

print x
print z
