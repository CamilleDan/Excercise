# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import json
from collections import Counter
from matplotlib import pylab
from matplotlib import pyplot as plt


#t1=pd.read_table(r"C:\pycharm\pydata-book-2nd-edition\datasets\bitly_usagov\example.txt")
#print t1
path=r"C:\pycharm\pydata-book-2nd-edition\datasets\bitly_usagov\example.txt"
#print open(path).readline()
records=[json.loads(line) for line in open(path)]
print records[0]
print records[0]['tz']
#对时区进行计数
time_zones=[rec['tz'] for rec in records if 'tz' in rec]
print time_zones[:10]
def get_counts(time_zones):
    counts={ }
    for x in time_zones:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts

counts=get_counts(time_zones)
print len(time_zones)
print counts['America/New_York']
#获取计数值前十位的时区
def top_ten_counts(count_dict,n=10):
    value_key_pairs=sorted(count_dict.items(),key=lambda d:d[1],reverse=True)
    #key表示用列表元素的某个属性和函数进行作为关键字。d表示dict中的一个元素，e[0]表示按键排序，e[1]则表示按值排序。reverse=False可以省略，默认为升序排列。
    return value_key_pairs[:n]

top10_tz=top_ten_counts(counts)
print top10_tz

#使用collection Counter类进行寻找前十时区
cnt = Counter()

for tz in time_zones:
    cnt[tz] += 1
print cnt

#用pandas进行时区计数
frame=pd.DataFrame(records)
#print frame
#print frame['tz'][:10]
tz_counts=frame['tz'].value_counts()
print tz_counts[:10]
#使用matplotlib生成图片
clean_tz=frame['tz'].fillna('Missing')
#print clean_tz
clean_tz[clean_tz==' ']='Unknow'
#print  clean_tz[:10]
tz_counts1=clean_tz.value_counts()
print tz_counts1[:10]
#画图
fig=plt.figure()
tz_counts1[:10].plot(kind='barh',rot=0)
plt.show()


# #解析agent信息
# a=frame['a']
# print a