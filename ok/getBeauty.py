#  -*- coding: utf-8 -*- 
'''
@Copyright © 2017 sanbo Inc. All rights reserved.
@Description: 下载美女图片，大图不要缩略图{调整代码结构}
@Version: 1.0
@Create: 2017年1月2日 上午3:17:31 
@Author: sanbo
'''
from bs4 import BeautifulSoup  
import urllib2  
import os
from __builtin__ import str

'''
    解析高清地址,并且去下载
'''

def test(i, urls):
    urls = ['http://www.4j4j.cn/beauty/20533.html', 'http://www.4j4j.cn/beauty/20532.html', 'http://www.4j4j.cn/beauty/20528.html', 'http://www.4j4j.cn/beauty/20525.html', 'http://www.4j4j.cn/beauty/20589.html', 'http://www.4j4j.cn/beauty/20524.html', 'http://www.4j4j.cn/beauty/20523.html', 'http://www.4j4j.cn/beauty/20521.html', 'http://www.4j4j.cn/beauty/20518.html', 'http://www.4j4j.cn/beauty/20515.html', 'http://www.4j4j.cn/beauty/20513.html', 'http://www.4j4j.cn/beauty/20511.html', 'http://www.4j4j.cn/beauty/20508.html', 'http://www.4j4j.cn/beauty/20582.html', 'http://www.4j4j.cn/beauty/20504.html', 'http://www.4j4j.cn/beauty/20502.html', 'http://www.4j4j.cn/beauty/20501.html', 'http://www.4j4j.cn/beauty/20498.html', 'http://www.4j4j.cn/beauty/20496.html', 'http://www.4j4j.cn/beauty/20492.html', 'http://www.4j4j.cn/beauty/20489.html', 'http://www.4j4j.cn/beauty/20488.html', 'http://www.4j4j.cn/beauty/20487.html', 'http://www.4j4j.cn/beauty/20628.html', 'http://www.4j4j.cn/beauty/20627.html', 'http://www.4j4j.cn/beauty/20480.html', 'http://www.4j4j.cn/beauty/20479.html', 'http://www.4j4j.cn/beauty/20476.html', 'http://www.4j4j.cn/beauty/20474.html', 'http://www.4j4j.cn/beauty/20610.html', 'http://www.4j4j.cn/beauty/20471.html', 'http://www.4j4j.cn/beauty/20469.html', 'http://www.4j4j.cn/beauty/20466.html', 'http://www.4j4j.cn/beauty/20462.html', 'http://www.4j4j.cn/beauty/20460.html', 'http://www.4j4j.cn/beauty/20457.html', 'http://www.4j4j.cn/beauty/20455.html', 'http://www.4j4j.cn/beauty/20452.html', 'http://www.4j4j.cn/beauty/20449.html', 'http://www.4j4j.cn/beauty/20444.html', 'http://www.4j4j.cn/beauty/20443.html', 'http://www.4j4j.cn/beauty/20441.html', 'http://www.4j4j.cn/beauty/20440.html', 'http://www.4j4j.cn/beauty/20643.html', 'http://www.4j4j.cn/beauty/20642.html', 'http://www.4j4j.cn/beauty/20641.html', 'http://www.4j4j.cn/beauty/20640.html', 'http://www.4j4j.cn/beauty/20639.html', 'http://www.4j4j.cn/beauty/20638.html', 'http://www.4j4j.cn/beauty/20637.html', 'http://www.4j4j.cn/beauty/20636.html', 'http://www.4j4j.cn/beauty/20635.html', 'http://www.4j4j.cn/beauty/20633.html', 'http://www.4j4j.cn/beauty/20632.html', 'http://www.4j4j.cn/beauty/20630.html', 'http://www.4j4j.cn/beauty/20629.html', 'http://www.4j4j.cn/beauty/20624.html', 'http://www.4j4j.cn/beauty/20623.html', 'http://www.4j4j.cn/beauty/20622.html', 'http://www.4j4j.cn/beauty/20620.html', 'http://www.4j4j.cn/beauty/20618.html', 'http://www.4j4j.cn/beauty/20614.html', 'http://www.4j4j.cn/beauty/20613.html', 'http://www.4j4j.cn/beauty/20612.html', 'http://www.4j4j.cn/beauty/20611.html', 'http://www.4j4j.cn/beauty/20608.html', 'http://www.4j4j.cn/beauty/20607.html', 'http://www.4j4j.cn/beauty/20606.html', 'http://www.4j4j.cn/beauty/20605.html', 'http://www.4j4j.cn/beauty/20603.html', 'http://www.4j4j.cn/beauty/20600.html', 'http://www.4j4j.cn/beauty/20599.html', 'http://www.4j4j.cn/beauty/20597.html', 'http://www.4j4j.cn/beauty/20596.html', 'http://www.4j4j.cn/beauty/20595.html', 'http://www.4j4j.cn/beauty/20594.html', 'http://www.4j4j.cn/beauty/20593.html', 'http://www.4j4j.cn/beauty/20592.html', 'http://www.4j4j.cn/beauty/20591.html', 'http://www.4j4j.cn/beauty/20585.html']
    for i in range(len(urls)):
        process(urls[i])

def process(url):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1',
        }
        content = urllib2.urlopen(urllib2.Request(url, None, header), data=None, timeout=3).read()
        soup = BeautifulSoup(content, "lxml")
        someData = soup.select("div.pic-image img")
        for some in someData:
            tempUrl = some['src']
            download(tempUrl)
    except Exception, e:
        print  str(e)
'''
增加去重,增加解析大图片详情地址
'''
def getUrls(n):
    url = 'http://www.4j4j.cn/beauty/tag_3_' + str(n) + '.html' 
    print url
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    html = urllib2.urlopen(urllib2.Request(url, None, header), data=None, timeout=3).read()
    soup1 = BeautifulSoup(html, "lxml")
    someData = soup1.select("div.i-list li a")
    allUrls = []  
    for some in someData:
        tempUrl = some['href']
        if "javascript" not in tempUrl:
            if tempUrl not in allUrls:
                allUrls.append(tempUrl);
    return allUrls

def download(url):
    try: 
        global number  
        number += 1
        path = 'D:/girls/'
    #    #如果没有文件夹则创建
    #    if not  os.path.exists(path):
    #        #貌似linux 是 os.path.mkdir(path)
    #        #os.mkdir(path)
    #        os.mkdir(path)
        #content = urllib2.urlopen(url).read()
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1',
        }
        request = urllib2.Request(url, None, header)
        content = urllib2.urlopen(request, data=None, timeout=3).read()
        filename = path + str(number) + '.jpg'  
        print 'download [' + filename + ']===>' + url
        #print 'download [' + filename + ']'
        f = open(filename, 'wb') #这种模式可以正常下载图片
        f.write(content)
        f.flush()
        f.close() 
    except Exception, e:
        print  str(e)
      
if __name__ == '__main__':
    number = 0
    path = 'D:/girls/'
    #如果没有文件夹则创建
    if not  os.path.exists(path):
        #貌似linux 是 os.path.mkdir(path)
        #os.mkdir(path)
        os.mkdir(path)
    for i in range(1, 75):
        try:
            print '开始爬第' + str(i) + ' 页'
            urls = getUrls(i)
            print '(' + str(len(urls)) + ') ' + str(urls)
            for u in range(len(urls)):
                try:
                    url = urls[u]
                    process(url) 
                except Exception, e:
                    print e
        except Exception, e:
            print e    
    print '爬完了～～！'
