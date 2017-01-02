#  -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup  
import urllib2  
  
  
'''
                    糗百爬虫
'''
  
def getContent(n):  
    url = 'http://www.qiushibaike.com/text/page/' + str(n) + '/'  
    #  url = 'http://www.qiushibaike.com/8hr/page/'+str(n)+'/'  
    print url  
    header = {  
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://www.qiushibaike.com/',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': '_xsrf=2|db27040e|6b4ed8d9536590d4ec5d2064cc2bef4f|1474364551; _qqq_uuid_="2|1:0|10:1474364551|10:_qqq_uuid_|56:MzBlNWFkOGE3MWEyMzc1MWIxMTE3MDBlZjM2M2RkZWQxYzU5YTg1Yw==|1dd2a4f4ceacad26b5da9cc295d2965226ea25ee73289855cf032629c4992698"; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1474364592; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1474364595; _ga=GA1.2.1125329542.1474364596'  
    }  
    content = urllib2.urlopen(urllib2.Request(url, None, header), data=None, timeout=3).read()
    soup = BeautifulSoup(content, "lxml")
    someData = soup.select("div.content span")  
    num = 0  
    for some in someData:  
        num = num + 1  
#        print num  
        print some.text + '\n'  

if __name__ == "__main__":  
    for i in range(1, 36):  
        getContent(i)  
