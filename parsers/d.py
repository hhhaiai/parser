#  -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup  
import urllib2  
import re  
  
  
def getGirlUrl(n):  
    url = 'http://www.4j4j.cn/beauty/tag_3_' + str(n) + '.html'  
    print 'getGirlUrl:' + url  
    response = urllib2.urlopen(url)  
    html = response.read()  
    soup1 = BeautifulSoup(html, "lxml")
#    缩略图
    someData = soup1.select("div.i-list li a img")
    allUrls = []  
    for some in someData:
        #这个取得是缩略图不是大图
        allUrls.append(some['data-original'])
    return allUrls  
  
  
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
#    print '[' + filename + ']===>' + url
    print '[' + filename + ']'
#    f = open(filename, 'w+')  
    f = open(filename, 'wb')  #增加这行貌似window就不乱码了
    f.write(content)
    f.flush()
    f.close()  
  
  
if __name__ == "__main__":  
    number = 0  
#    getGirlUrl(1)  
#    for i in range(1, 2):  
    for i in range(1, 75):  
        urls = getGirlUrl(i)  
        for u in range(1, len(urls)):  
            download(urls[u])  
        print '正在爬第' + str(i) + '页'  
    print '爬完了～～！'  
