# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:31:32 2018

@author: Administrator
"""

print 'round1'

import urllib2,cookielib#load repository

url='http://www.baidu.com/'#set url
response1=urllib2.urlopen(url)#creat object
print response1.getcode()#get statuscode
print len(response1.read())# get length of web

print 'round2'
request=urllib2.Request(url)
request.add_header('userAgent','Mozilla/5.0')
response2=urllib2.urlopen(request)#creat object
print response2.getcode()#get statuscode
print len(response2.read())# get length of web

#失败了
print 'round3'
cj = cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3=urllib2.urlopen(url)#creat object
print response3.getcode()
print response3.read()
print cj
########################################

from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,#document
                   'html.parser',#parser
                   from_encoding='utf-8')
soup.find_all('a')#找所有标签
soup.find_all('a',href='')#找所有属性为href内容的标签
soup.find('a')#只找一个标签
node.name#获取节点名称
node['href']#获取节点属性
node.get_text()#获取节点文字


################################
from bs4 import BeautifulSoup 

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,#document
                   'html.parser',#parser
                   from_encoding='utf-8')#coding

print 'get links'
links=soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

print 'get lacie link'
link_node=soup.find('a',href='http://example.com/lacie')
print link_node.name,link_node['href'],link_node.get_text()

print ''
import re
link_node=soup.find('a',href=re.compile(r'ill'))
print link_node.name,link_node['href'],link_node.get_text()

print 'get p'
p_node=soup.find('p',class_='title')
print p_node.name,p_node.get_text()

















