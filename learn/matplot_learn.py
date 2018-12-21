# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

import numpy as np
import matplotlib.pyplot as plt

# 创建等差数列
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # 创建-π~π等差数组，265个，最后的点计算在内
# 创建函数
c, s = np.sin(x), np.cos(x)
# 创建图形窗口
plt.figure(1)
# 绘图
plt.plot(x, c, color='blue', linewidth=1.0, linestyle='-', label='cos', alpha=0.5)
plt.plot(x, s, 'r.', label='sin')  # r表示红色，.表示线型
# 添加图标题
plt.title('cos&sin')
# 图片展示
# plt.show()
# 调用图表框模块
ax = plt.gca()
# 选择图表框线并设置颜色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
# 设置图标轴位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],  # 标识位置
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])  # 标识内容
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.5))
plt.legend(loc='upper left')  # 图例
plt.grid()  # 网格线
# plt.axis([-1,1,-0.5,1])#显示范围横轴、纵轴
plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color='green')  # x表示横轴，<0.5表示判断，c表示纵轴
t = 1
plt.plot([t, t], [0, np.cos(t)], 'y', linewidth=3, linestyle='--')

# scartt
fig = plt.figure()
ax = fig.add_subplot(3, 3, 1)  # 画布分为3*3分显示在第一格
n = 128
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(X, Y)  # 颜色
# plt.axes([0.025,0.025,0.95,0.95])#显示范围
ax.scatter(X, Y, s=75, c=T, alpha=.5)  # 散点图，c为颜色，颜色可用数值表示
plt.xlim(-1.5, 1), plt.xticks([])  # 显示的x范围
plt.ylim(-1.5, 1), plt.yticks([])  # 显示的y的范围
plt.axis()  # ？？？
plt.title('scatter')
plt.xlabel('x')
plt.ylabel('y')

# bar
fig.add_subplot(332)
n = 10
x = np.arange(n)
y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1, n)
y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1, n)

plt.bar(x, +y1, facecolor='#9999ff', edgecolor='white')
plt.bar(x, -y2, facecolor='#ff9999', edgecolor='white')
# 添加注释
for a, b in zip(x, y1):
    plt.text(a + 0.4, b + 0.05, '%.2f' % b, ha='center', va='bottom')
for a, b in zip(x, y2):
    plt.text(a + 0.4, -b - 0.05, '%.2f' % b, ha='center', va='top')

# pie
fig.add_subplot(3, 3, 3)
n = 20
z = np.ones(n)
z[-1] *= 2
plt.pie(z, explode=z * 0.5, colors=['%f' % (i / float(n)) for i in range(n)],
        labels=['%.2f' % (i / float(n)) for i in range(n)])
plt.gca().set_aspect('equal')
plt.xticks([]), plt.yticks([])

# polar
fig.add_subplot(3, 3, 4, polar=True)
n = 20
theta = np.arange(0, 2 * np.pi, 2 * np.pi / n)
radii = 10 * np.random.rand(n)
plt.polar(theta, radii)
# heatmap
fig.add_subplot(3, 3, 5)
from matplotlib import cm

data = np.random.rand(3, 3)
cmap = cm.Blues
map = plt.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto', vmin=0, vmax=1)
# 3d
from mpl_toolkits.mplot3d import Axes3D

ax = fig.add_subplot(3, 3, 6, projection='3d')
ax.scatter(1, 1, 3, s=100)
# hot map
fig.add_subplot(3, 1, 3)


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
c, d = np.meshgrid(x, y)
plt.contourf(c, d, f(c, d), 8, alpha=0.75, cmap=plt.cm.hot)
plt.savefig('./data/fig.png')
plt.show()
