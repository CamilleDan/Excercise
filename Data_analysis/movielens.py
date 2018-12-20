# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import json
from collections import Counter
from matplotlib import pylab
from matplotlib import pyplot as plt

# MovieLens
path1 = r"C:\pycharm\pydata-book-2nd-edition\datasets\movielens\users.dat"
path2 = r"C:\pycharm\pydata-book-2nd-edition\datasets\movielens\ratings.dat"
path3 = r"C:\pycharm\pydata-book-2nd-edition\datasets\movielens\movies.dat"

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(path1, sep='::', header=None, names=unames, engine='python')
rnames = ['user_id', 'movie_id', 'rate', 'timestamp']
ratings = pd.read_table(path2, sep='::', header=None, names=rnames, engine='python')
mnames = ['movie_id', 'title', 'genrs']
movies = pd.read_table(path3, sep='::', header=None, names=mnames, engine='python')

print users[:5]
# print ratings[:5]
# print movies[:5]
# 融合多张表为一张表
data = pd.merge(pd.merge(ratings, movies), users)
print data.ix[0]
mean_ratings = data.pivot_table('rate', index='title', columns='gender', aggfunc='mean')
print mean_ratings[:5]
# 统计每个电影被评论的次数
ratings_by_title = data.groupby('title').size()
print ratings_by_title[:10]
active_titles = ratings_by_title.index[ratings_by_title > 250]
print active_titles[:10]

mean_ratings = mean_ratings.ix[active_titles]
top_female_titles = mean_ratings.sort_values(by='F', ascending=False)
print top_female_titles[:10]

# 计算评分分歧
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print sorted_by_diff[:10]
# 不考虑性别因素计算分差的标准差
# 根据电影名称分组得到得分数据的标准差
rating_std_by_title = data.groupby('title')['rating'].std()
# 根据active_titles进行过滤
rating_std_by_title = rating_std_by_title.ix[active_titles]
# 根据值对Series进行降序排列
print rating_std_by_title.order(ascending=False)[:10]
