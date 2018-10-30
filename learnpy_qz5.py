# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

#收集百度贴吧信息
#思路：打开网页先分析页面url（规律、总页数）
#2、获取邮箱

import urllib
import re

urls='https://tieba.baidu.com/p/5926553812?pn=%s'
i=0
emailurl = []
#访问网页
def emailhtml(url):
    html = urllib.urlopen(url).read()
    return html

#找最大页数
def emails(url):

    elem=r'<a href=".+?pn=(.+?)">尾页</a>'#正则表达式
    reg=re.compile(elem)#编译，参数为正则表达式字符串
    regs=re.findall(reg,emailhtml(url))#匹配对象
    return regs

#匹配邮箱
def email(url):
    text=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'#去邮箱地址的正则表达式
    reg=re.compile(text)
    return re.findall(reg,emailhtml(url))

while 1:
   i += 1
   if i<= emails(urls %i):
       print ('正在爬取第'+str(i)+'页内容')
       html = email(urls %i)
       emailurl += html
   else:
       break



fn=open('e:\demo\url.txt','a+')#路径，方式
for i in emailurl:
    fn.write(i+'\n')



