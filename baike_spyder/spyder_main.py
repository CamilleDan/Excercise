# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


######spyder_main
import url_manager,html_downloader,html_parser,html_outputer#引入功能模块

class SpiderMain(object):#总调度程序
    def __init__(self):#在各个函数中初始化所有功能模块
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutput()
   
    #调度程序
    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print 'craw %d: %s' % (count,new_url)
                html_count=self.downloader.download(new_url)
                new_urls,new_dara=self.parser.parse(new_url,html_count)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count==1000:
                    break
                
                count=count+1
            except:
                print 'craw failed'
                
        self.outputer.output_html()   
      
if __name__=='__main__':
    root_url='https://baike.baidu.com/item/Python'
    #设定入口URL
    obj_spider=SpiderMain()#设定main函数
    obj_spider.craw(root_url)#启动爬虫
      

    