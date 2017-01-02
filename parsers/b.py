#  -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup  
import urllib2  
import re  
from __builtin__ import file
  
'''
    爬美女图片
'''
  
def getGirlUrl(n):  
    url = 'https://tuchong.com/tags/%E7%BE%8E%E5%A5%B3?page=' + str(n)  
    print "getGirlUrl:" + url  
    response = urllib2.urlopen(url)  
    html = response.read()  
    soup1 = BeautifulSoup(html, "lxml")  
    #  someData = soup1.select("div.post-row")  
    someData = soup1.select("div.post-row div.post-collage a.theatre-view img")  
    allUrls = []  
    for some in someData:  
        allUrls.append(some['src'])  
    print allUrls
    return allUrls
  
  
  
  
def download(url):  
    path = 'D:/girls/'  
    content = urllib2.urlopen(url).read()  
    format = '[0-9]*\.jpg';  
    res = re.search(format, url);  
#    print 'downloading:', res.group()  
    filename = path + res.group()
#    f = file(filename, 'r+')
#    f = open(filename, 'r+')
    f = file(filename, 'wb')
#    f = open(filename, 'wb')  
    f.write(content)
    f.flush()
    f.close()  
  
  
  
  
if __name__ == "__main__":  
  
    for i in range(1, 5000):  
#    for i in range(1, 3):  
        urls = getGirlUrl(i)
        for u in range(1, len(urls)):  
            download(urls[u])  
        print '正在爬第' + str(i) + '页'  
