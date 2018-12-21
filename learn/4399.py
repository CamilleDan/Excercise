# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

# w网页结构
# 记录游戏详情页面
# 游戏预览图地址
import urllib
import re

url = r'http://www.4399.com/flash_fl/2_1.htm'


def get_html(url):
    html = urllib.urlopen(url).read()
    # print html.decode('gbk')
    return html


def get_url_list(html):
    # .表示除了换行符和制表符以外的任何字符
    # *表示前面的字符可以出现一次或无限次
    reg = '<img src="(.*?.jpg)">'
    reg = re.compile(reg)
    url_list = re.findall(reg, html)
    return url_list


def download_ing(url_list):
    x = 0
    for url in url_list:
        print url
        x += 1
        urllib.urlretrieve(url, 'c:\demo\game\%s.jpg' % x)
        print '正在下载第%d张图片' % x


html = get_html(url)
url_list = get_url_list(html)
download_ing(url_list)
