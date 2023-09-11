import requests
import os
import re
import time
from bs4 import BeautifulSoup

l=[]
cnt=0

def getpage(url):
    r=requests.get(url,headers=hd)
    fff=1
    while(r.status_code!=200 and fff<=3):
        r=requests.get(url,headers=hd)
        fff=fff+1
    return r.text


if __name__ == '__main__':
    print('Begin')
    fgx="\n--------------------------------------------------------------------\n"
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Host': 'book.douban.com',
        'Referer': 'https://search.douban.com/book/subject_search?'
    }
    url0="https://book.douban.com/subject/"
    begin=6872578
    #end=6872580
    end=6872607
    i=begin
    while(i<=end):
        xurl=url0+str(i)
        soup=BeautifulSoup(getpage(xurl),'html.parser')
        xxx=soup.find('h1').text
        yy=soup.find("div",attrs={"class":"intro"})
        if yy==None:
            yyy="没有简介"
        else:
            yyy=""
            yy=yy.find_all("p")
            for ii in yy:
                yyy+=ii.string
        l.append([xxx,yyy])
        print(i)
        i+=1
    with open('./result.txt', 'wb') as f:
        for iii in l:
            f.write(iii[0].encode())
            f.write(iii[1].encode())
            f.write(fgx.encode())
    print('OK')