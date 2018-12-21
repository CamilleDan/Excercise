# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
# 1、爬取到网页的内容
# 2、筛选内容（图片url）
# 3、通过url下载内容（执行情况要显示出来）
# 4、保存在本地
# src=''//img.hb.aicdn.com/
# 61bf8d9ffc062963febb71842c53fce61e126da818ae3-R74hzQ_sq320''
# 正则src=''.+?\.jpg


import urllib
import re


def gethtml(url):
    page = urllib.urlopen(url).read()  # 读取网页源码
    return page


#
def getimg(html):
    reg = r'src="(.+?\.jpg)"'  # 匹配对应的HTML代码
    imgre = re.compile(reg)  # 将对应编码解压
    imglist = re.findall(imgre, html)  #
    x = 0
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl, 'e:\demo\%s.jpg' % x)

        x += 1


#
html = gethtml('http://588ku.com/')
getimg(html)
