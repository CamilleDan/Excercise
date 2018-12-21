# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
import os, time

s = ['博览群书', '努力去开拓自己的多样性']  # 定义字符串列表
fn = r'E:\demo\nihao.txt'  # 把文件路径赋值给变量方便调用


def write_words():  # 定义一个函数方便调用
    a = open(fn, 'w')  # 写文件内容
    a.write('博览群书，努力去开拓自己的多样性吧！')
    a.close()  # 关闭文件
    print '未找到文件，已写入新文件'


def read_words():
    cont = open(fn, 'r').read()  # 读文件的内容
    return cont


def change_words():
    a = open(fn, 'w')
    a.write('博览群书，努力去开拓自己的多样性吧！')
    a.close()
    print '文件被篡改，已改正'


while 1:
    time.sleep(1)
    if os.path.exists(fn):  # 判断文件是否存在
        cont = read_words()
        if cont.find(s[0]) != -1 and cont.find(s[1]) != -1:  # 判断关键字是否存在
            print '关键字全部存在'
        else:
            change_words()
    else:
        write_words()
