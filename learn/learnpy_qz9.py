# -*- coding:utf-8 -*-


import urllib, urllib2
import re

url = 'https://www.hotread.com/story/1010647'


# <a href="//www.hotread.com/story/1010209/1001170204">楔子</a>

def getlinks(url):
    html = urllib.urlopen(url).read()  # 为了获取各章节的链接和标题
    reg = r'<a href="//(.+?)">(.+?)</a>'  # 加括号的正则部分可以被返回，不加括号不会被返回
    reg = re.compile(reg)  # 编译后的正则效率会提高
    link = re.findall(reg, html)  # 在源代码里匹配正则表达式
    return link


links = getlinks(url)


def getcontent(link):
    html = urllib.urlopen(link.read())
    reg = r'<div class="content">([\s\S]*)<p class="alter alter-info">'
    reg = re.compile(reg)
    content = re.findall(reg, html)
    return content


def writecontent(link, name):
    content = getcontent(link)
    file = open('c:\\demo\%s.html' % name, 'w')
    file.close()


for link in links:
    writecontent(link[0], link[1])
