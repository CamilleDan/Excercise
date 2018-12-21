# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""

# 收集百度贴吧信息
# 思路：打开网页先分析页面url（规律、总页数）
# 2、获取邮箱

import urllib
import re
import smtplib
from email.mime.text import MIMEText

urls = 'https://tieba.baidu.com/p/5926553812?pn=%s'
i = 0
emailurl = []


# 访问网页
def emailhtml(url):
    html = urllib.urlopen(url).read()
    return html


# 找最大页数
def emails(url):
    elem = r'<a href=".+?pn=(.+?)">尾页</a>'  # 正则表达式
    reg = re.compile(elem)  # 编译，参数为正则表达式字符串
    regs = re.findall(reg, emailhtml(url))  # 匹配对象
    return regs


# 匹配邮箱
def email(url):
    text = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'  # 去邮箱地址的正则表达式
    reg = re.compile(text)
    return re.findall(reg, emailhtml(url))


while 1:
    i += 1
    end = int(emails(urls))
    if i <= end:
        print ('正在爬取第' + str(i) + '页内容')
        html = email(urls % i)
        emailurl += html
    else:
        break

# fn=open('e:\demo\url.txt','a+')#路径，方式
# for i in emailurl:
#     fn.write(i+'\n')
# f.close()
print('总共爬取到%s个邮箱地址' % len(emailurl))

mail_host = 'smtp.aliyun.com'
mail_username = 'litianqiang@aliyun.com'
mail_password = 'tanzhou123'


def get_mail(to_mail, _text):  # 定义邮件
    my = 'hello,' + mail_username
    msg = MIMEText(_text, _subtype='html', _charset='utf-8')  # 格式化,发送邮件时使用的参数
    msg['To'] = ';'.join(to_mailm)
    msg['From'] = my
    msg
    ''[Subject] = '同学你好'

    try:
        s = smtplib.SMTP()  # 把发送邮件赋值到变量上显示错误代码
        s.connect(mail_host)  # 连接邮件服务器
        s.login(mail_username, mail_password)  # 登录邮件服务器
        s.sendmail(my, to_mail, msg, as_string())  # 发件人、收件人、内容、
        s.close()
        return True

    except:
        print str(s)
        return False


me = '<a  href="http://www.tanzhhouedu.com">这里有ps视频'

i = 0
while 1:
    if i <= end:
        maillist = emailurl[i]
        i += 1
        if get_mail(maillist, me):
            print '发送成功'
        else:
            print '发送失败'
