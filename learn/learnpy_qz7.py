# -*- coding:utf-8 -*-

from Tkinter import *  # 可创建窗口的包
import tkMessageBox  # 可现实弹窗的包
import urllib, urllib2  # 爬去网页内容包
import re  # 正则表达式包


# 加载图片
def img(name):
    photo = PhotoImage(file='%s.gif' % name, width='500', height='300')  # 设置图片存储位置和尺寸
    a2 = Label(image=photo)  # 在窗口创建label
    a2.image = photo  # 将图片赋给label
    a2.grid(row=0, column=10)
    # root.mainloop(1)


# 请求网址
def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    html = urllib2.urlopen(url, data)
    return html.read()  # 网页源代码


# 调度程序
def cu():
    if e1.get() == "":
        tkMessageBox.showinfo("错误", "请先输入姓名！")
    else:
        url = "http://www.jiqie.com/a/re22.php"
        name = e1.get()
        name = name.encode("utf-8")
        data = {"id": name,
                "id_": "pihun",
                "i_d": "jiqie",
                "id1": "30",
                "id2": "905",
                "id3": "#0000FF",
                "id4": "#0000DD",
                "id5": "#0000AA",
                "id6": "#000077"}
        text = post(url, data)
        # print(text)
        # tkMessageBox.showinfo("签名设计","处理完成，请查看签名！")
        reg = re.compile(r'<img src="\.\./i/(.+?)">')  # 编译正则表达式
        reg = re.findall(reg, text)  # 在源代码中匹配正则表达式
        imgurl = "http://www.jiqie.com/i/" + reg[0]
        name = name.decode("utf-8")
        urllib.urlretrieve(imgurl, name + ".gif")  # 将远程数据下载到本地：下载路径，filename
        img(name)


# 创建窗口
top = Tk()  # 把窗口赋值给top变量
top.title('设计个性签名')  # 窗口title
top.geometry('+600+400')  # 窗口长度x窗口宽度+横坐标+纵坐标
top.resizable(width=False, height=False)  # 可更改宽高
# 创建窗口标签
a1 = Label(top, text='姓名', font='黑体，15')  # 创建标签：选择窗口，标签内容
a1.grid(row=0, column=0, sticky='news')  # 标签位置，通过表格的方式来布局:行，列(会自动忽略被未占用的位置)
# 创建文本框
e1 = Entry(top)  # 创建输入文本框
e1.grid(row=0, column=1)  # 文本框位置
# 创建按钮
b = Button(top, text='一键设计签名', command=cu)  # 按钮，按钮文字，回调函数
b.grid(row=3, column=1)  # 按钮位置

top.mainloop()  # 不停循环给系统发消息（在桌面创建一个窗口）
