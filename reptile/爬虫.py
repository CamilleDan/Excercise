# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
# https://movie.douban.com/subject/26985127/
import urllib, urllib2
import re

url = 'http://huaban.com/'


def get_html(url):
    html = urllib.urlopen(url).read()
    return html


def download_img(html):
    reg = r'data-src="(.*?)"'
    reg = re.compile(reg)
    urls = re.findall(reg, html)
    x = 0
    for url in urls:
        x += 1
        urllib.urlretrieve(url, 'e:\demo\%s.jpg' % x)
        print '正在下载第%d张图片' % x


html = get_html(url)
download_img(html)
