#  -*- coding: utf-8 -*- 
'''
@Copyright © 2017 sanbo Inc. All rights reserved.
@Description: 下载美女图片，大图不要缩略图
@Version: 1.0
@Create: 2017年1月2日 上午3:17:31 
@Author: sanbo
'''
from bs4 import BeautifulSoup  
import urllib2  
import re  
from _nsis import allusers



def process(url):
    response = urllib2.urlopen(url) 
    html = response.read()  
    soup1 = BeautifulSoup(html, "lxml")
    #    缩略图
    someData = soup1.select("div.pic-image img")
    allUrls = []
    for some in someData:
        tempUrl = some['src']
        if tempUrl not in allUrls:
            print "process:" + tempUrl
            download(tempUrl)
    
'''
增加去重,增加解析大图片详情地址
'''
def getUrls(n):
    url = 'http://www.4j4j.cn/beauty/tag_3_' + str(n) + '.html' 
#    url = "http://www.4j4j.cn/beauty/tag_3_1.html"
    print 'getGirlUrl:' + url  
    response = urllib2.urlopen(url)  
    html = response.read()  
    soup1 = BeautifulSoup(html, "lxml")
    #    缩略图
    someData = soup1.select("div.i-list li a")
    allUrls = []  
    for some in someData:
        tempUrl = some['href']
        #这个取得是缩略图不是大图
        if "javascript" not in tempUrl:
#            print some['href']
            if tempUrl not in allUrls:
                print "getUrls url:" + tempUrl
                process(tempUrl)

def download(url):  
    global number  
    number += 1  
    path = 'D:/girls/'
#    content = urllib2.urlopen(url).read()
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    request = urllib2.Request(url, None, header)
    content = urllib2.urlopen(request).read()
    filename = path + str(number) + '.jpg'  
    print 'download [' + filename + ']===>' + url
#    f = open(filename, 'w+')  
    f = open(filename, 'wb')  #增加这行貌似window就不乱码了
    f.write(content)
    f.flush()
    f.close() 
      
if __name__ == '__main__':
    number = 1
    for i in range(1, 75):
        getUrls(i)
#        print allRR
#        for u in range(1, len(tempURL)):
#            allUrls = process(tempURL[u])
#            for qq in range(1, len(allUrls)):  
#                download(allUrls[qq])      
