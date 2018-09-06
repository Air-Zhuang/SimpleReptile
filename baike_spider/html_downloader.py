# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/29 21:20'
import urllib2
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        response=urllib2.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()