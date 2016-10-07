# -*-coding:utf8-*-
import urllib2
import cookielib
import os

fileName = 'cookie.txt'
# cookie = cookielib.CookieJar()
cookie = cookielib.MozillaCookieJar(fileName)
# 保存到文件
if os.path.exists(fileName):
    cookie.load(fileName, ignore_discard=True, ignore_expires=True)

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
url = "http://www.baidu.com"
request = urllib2.Request(url)
response = opener.open(request)

cookie.save(ignore_discard=True, ignore_expires=True)

cookie.load(fileName, ignore_discard=True, ignore_expires=True)
# for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value