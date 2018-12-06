# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
#生成英文词云图
from wordcloud import WordCloud
import matplotlib.pyplot as plt

f = open(u'E:\dataset\my_test1.txt','r').read()

wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('E:\dataset\my_test1.png')
