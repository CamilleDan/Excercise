# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:10:17 2018

@author: Administrator
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class HtmlOutput(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return 
        self.data.append(data)
        
    def output_html(self):  
        print self.datas
#        fout=open('output.html','w')
#        fout.write('<html>')
#        fout.write('<body>')
#        fout.write('<table>')
#        
#        for data in self.datas:
#            fout.write('<tr>')
#            fout.write('<td>%s</td>'%data['url'])
#            fout.write('<td>%s</td>'%data['title'].encode('utf-8'))
#            fout.write('<td>%s</td>'%data['summary'].encode('utf-8'))
#            fout.write('</tr>')
#        
#        fout.write('</table>')
#        fout.write('</body>')
#        fout.write('</html>')
#        
#        fout.close()