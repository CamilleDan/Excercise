# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

import pandas as pd

# 读取数据文件
data = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex1.csv')
print(data)
data1 = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex1.csv', header=None)
print(data1)
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex1.csv', index_col='message')
data2 = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\csv_mindex.csv', index_col=['key1', 'key2'])
print(data2)

url = r'E:\dataset\pydata-book-2nd-edition\examples\ex3.txt'
file = open(url)
list(file)
data3 = pd.read_table('E:\dataset\pydata-book-2nd-edition\examples\ex3.txt', sep='\s+')
print(data3)
data4 = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex4.csv')
print(data4)
data4 = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex4.csv', skiprows=[0, 2, 3])
data5 = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex5.csv')
# data5=pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex5.csv',na_values=['Null','Nan'])
print(data5)
sentinels = {'something': 'one', 'c': 'Nan', 'message': 'Nan'}
data5 = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex5.csv', na_values=sentinels)
print(data5)
data6 = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex6.csv', nrows=5)
print(data6)
chunker = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\ex6.csv', chunksize=1000)
print(chunker)
tot = pd.Series([])
choukercount = 0
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
    choukercount += 1
tot = tot.value_counts(ascending=False)
print(tot)
print(choukercount)
print(len(data6))
print(data6)

data6.to_csv(r'E:\dataset\pydata-book-2nd-edition\examples\out.csv')  # 将数据写出到csv格式
