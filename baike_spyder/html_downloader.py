 #-*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:09:56 2018

@author: Administrator
"""

import urllib2
class HtmlDownloader(object):
        
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()