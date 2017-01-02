#  -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup  
import urllib2  
import csv  
import sys  

'''
    爬资质
http://blog.csdn.net/guiguzi1110/article/details/52679895
'''
def getSomePageMd5(i):  
    url = 'http://hospital.yuemei.com/rate/shanghai/p' + str(i) + ".html"  
    print url  
    response = urllib2.urlopen(url)  
    html = response.read()  
    soup1 = BeautifulSoup(html, "lxml")  
    someData = soup1.select("div.hosList div.hos-related")  
    for d in someData:  
        name = d.findChild("span", attrs={"class":"item1"}).find("a").text  
        zizhi_div = d.findChild("div", attrs={"class":"item2"})  
        zi = zizhi_div.findChild("div", attrs={"class":"inline"})  
        zizhi = ""  
        for s in zi.children:  
            zizhi += s.text + " "  
            address_div = d.findChild("span", attrs={"class":"item2"})  
            address = ""  
            for i in address_div:  
                address += i.text  
                #  print address  
                spamwriter.writerow([name, zizhi, address])  
            #  print name+"   "+zizhi+ "    "+address  
  
  
if __name__ == "__main__":  
        reload(sys)  
        sys.setdefaultencoding('utf8')  
        fff = open('ggz.csv', 'wb')  
        spamwriter = csv.writer(fff, dialect='excel')  
        spamwriter.writerow(["name", "zizhi", "address"])  
        #  getSomePageMd5()  
        for i in range(1, 11):  
            getSomePageMd5(i)  
