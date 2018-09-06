# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/28 22:27'

import urllib2,cookielib

#爬一个简单网页
response=urllib2.urlopen('http://www.baidu.com')
print response.getcode()
cont=response.read()
print len(cont)

#有头信息
request=urllib2.Request('http://www.baidu.com')
request.add_header("user-agent","Mozilla/5.0")
response3=urllib2.urlopen('http://www.baidu.com')
print response3.getcode()
cont3=response3.read()
print len(cont3)

#添加特殊情境的处理器
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response2=urllib2.urlopen("http://www.baidu.com")
print response2.getcode()
cont2=response2.read()
print len(cont2)

