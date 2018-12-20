# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import json
from collections import Counter
from matplotlib import pylab
from matplotlib import pyplot as plt

path = r"C:\pycharm\pydata-book-2nd-edition\datasets\babynames\yob1880.txt"

names = ['name', 'gender', 'births']
baby_names1880 = pd.read_table(path, sep=',', header=None, names=names)
print baby_names1880[:10]
print baby_names1880.groupby('gender').births.sum()
# 整合所有的babynames数据表
years = range(1880, 2011)
pieces = []

for year in years:
    path = r"C:\pycharm\pydata-book-2nd-edition\datasets\babynames\yob%d.txt" % year
    frame = pd.read_table(path, sep=',', header=None, names=names)
    frame['year'] = year
    pieces = pieces.insert(-1, frame)

names = pieces.concat(pieces, ignore_index=True)
print names.groupby('gender').births.sum()
