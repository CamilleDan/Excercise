# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
import numpy as np
import pandas as  pd
import pylab
import matplotlib.pyplot as plt

#figsize设置figure的大小，单位为英尺
fig5=plt.figure(figsize=[10,5])
ax=fig5.add_subplot(1,1,1)


# 创建画布
fig = plt.figure()
# 在画布内划分subplot
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
# 用ax1实例对象hist方法绘制柱图
ax1.hist(np.random.rand(100), bins=20, color='b', alpha=0.6)
# 用ax2实例对象scatter方法绘制散点图（x，y）
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.rand(30), color='b')
# 用ax3实例对象plot方法绘制折线图（数据，颜色线型简写，标记）
ax3.plot(np.random.randn(50).cumsum(), 'k--', marker='o')
# figure对象savefig方法保存图片（路径/filename，像素，图片白边多少）
fig.savefig('E:/dataset/p1.png', dpi=400, bbox_inches='tight')


# 生成一个空画布
fig1 = plt.figure()
# figure对象的add_subplot方法将当前画布划分为2*2并且选中第一块
axes = fig1.add_subplot(2, 2, 1)
# 用axes对象plot方法绘制折线图（数据，颜色线型简写）
axes.plot(np.random.randn(50).cumsum(), 'k--')
# 用ax2对象hist方法绘制柱图
axes2 = fig1.add_subplot(2, 2, 2)
axes2.hist(np.random.rand(10))
# 用axes3对象scatter方法绘制散点图（x，y）
axes3 = fig1.add_subplot(2, 2, 3)
axes3.scatter(np.random.rand(10), np.random.rand(10))


# 简写方式同时创建figure和2*2subplot
fig2, axes = plt.subplots(2, 2)
# 可通过索引绘制subplot
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=40, color='b', alpha=0.6)
# 调整subplot外部的高级函数。wspace、hspace控制subplot外部宽和高的百分比
plt.subplots_adjust(wspace=0.2, hspace=0.2)


fig3,ax4=plt.subplots(1,1)
# plot参数（数据，颜色，标记，线型，图例文字）
plt.plot(np.random.rand(10), color='b', marker='o', linestyle='--', label='default')
# plt的legend方法添加图例（选择图例位置best为最佳位置）图例字体在plot方法的label参数设置
plt.legend(loc='best')
# plt的xlim方法设置x轴长度第一个参数类型为list
plt.xlim([-1, 10])


# figure axes 简写创建画布和subplot
fig4, axes4 = plt.subplots(1, 1)
# 在同一张图上绘制三条折线
axes4.plot(np.random.randn(100).cumsum(), 'b--', label='one')
axes4.plot(np.random.randn(100).cumsum(), 'k--', label='two')
axes4.plot(np.random.randn(100).cumsum(), 'r--', label='three')
axes4.legend(loc='best')
# set_xticks、set_xticklabels方法设置x轴刻度位置、x轴刻度标签（rotation旋转角度，字体大小）
axes4.set_xticks([0, 20, 40, 60, 80])
axes4.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
axes4.set_title('my first plot')
axes4.set_xlabel('x label')
# axes的text方法添加注解（添加位置,注释文字，字体，字号）
axes4.text(20, 0, 'hello world', family='monospace', fontsize=7,color='black')
axes4.annotate('hello world',xy=(100,0),xytext=(100,0),arrowprops=dict(facecolor='black',horizontalaligment='left'))


# 07年标准普尔500指数价格实战
from _datetime import datetime
fig6=plt.figure()
ax=fig6.add_subplot(1,1,1)

data = pd.read_csv(r'E:\dataset\pydata-book-2nd-edition\examples\spx.csv', parse_dates=True, index_col=0)
spx = data['SPX']
print(spx)

spx.plot(style='k--',label='crisis price')
crisis_data = [(datetime(2007, 10, 11), 'peak of bull market'),
               (datetime(2008, 3, 12), 'bear stearn fails'),
               (datetime(2008, 9, 15), 'lehman')]
for date,label in crisis_data:
    #(注释文本，被注释的坐标点，注释文本的坐标点，注释标记形状)
    ax.annotate(label,xy=(date,spx.asof(date)+80),xytext=(date,spx.asof(date)+200),
                arrowprops=dict(facecolor='black'),horizontalalignment='left',verticalalignment='top')
                # 箭头的样式，dict（字典）型数据，如果该属性非空，则会在注释文本和被注释点之间画一个箭头
                # horizontalalignment、verticalalignment注释文本的左端和低端对齐到指定位置
ax.set_xlim('1/1/2007','1/1/2011')
ax.set_ylim([600,1800])
ax.set_xlabel('time')
ax.set_xlabel('time')
ax.set_ylabel('price')
ax.set_title('Important dates in 2008-2009 financial crisis')
ax.legend(loc='best')


# 画图形
fig5=plt.figure()
axes5=fig5.add_subplot(1,1,1)
rect=plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)
circ=plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)
pgon=plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color='g',alpha=0.5)

axes5.add_patch(rect)
axes5.add_patch(circ)
axes5.add_patch(pgon)


# pandas内置绘图函数,Series绘图方法
fig7,axes6=plt.subplots(2,1)
df = pd.Series(np.random.randn(10), index=np.arange(0, 100, 10))
#ylim指定y轴范围，ax指定绘制在哪个subplot上，grid指定是否显示网格线
df.plot(ylim=[-2,2],grid=True)
df.plot(kind='bar',ax=axes6[0],color='k',alpha=0.7)
df.plot(kind='barh',ax=axes6[1],color='b',alpha=0.7)
# pandas内置绘图函数,dataframe绘图方法,columns自动变图例
df2=pd.DataFrame(np.random.randn(10,4),columns=list('abcd'),index=np.arange(0,100,10))
#stacked为True的时候显示堆积柱图，title设置图标题，stack指定是否是堆叠柱图
df2.plot(title='data frame plot')
df2.plot(kind='bar',title='data frame plot',stacked=True,alpha=0.5)

