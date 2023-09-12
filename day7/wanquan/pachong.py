from asyncio import ensure_future
from bs4 import BeautifulSoup
import requests
import json
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
}
num=6872578
x=0
lis=[]
for i in range(30):
    content=requests.get(f"https://book.douban.com/subject/{num+i}/",headers=headers).text

    soup=BeautifulSoup(content,"html.parser")
    if(soup==None):
        continue
    x+=1

    title=soup.find("h1")
    if(title==None):
        continue
    title=title.find("span")
    if(title==None):
        continue


    intro=soup.find("span",attrs={"class":"all hidden"})
    if intro==None:
        intro_all="暂无简介"
    else:
        intro=intro.find("div",attrs={"class":"intro"})
        intro_all=""
        intro=intro.find_all("p")
        for intro_every in intro:
            intro_all+=intro_every.string
    
    author=soup.find("div",attrs={"class":"related_info"})
    if(author==None):
        author_all="暂无作者简介"
    else:
        author=author.find("div",attrs={"class":"intro"})
    if(author==None):
        author_all="暂无作者简介"
    else:
        author_all=""
        author=author.find_all("p")
        for j in author:
            author_all+=j.string
    
    lis.append({"book_name":title.string,"introduction":intro_all,"author_introduction":author_all})

with open('./douban.json','w',encoding='utf-8') as fp:
    json.dump(lis , fp,ensure_ascii=False,indent=4,sort_keys=True)
    print('ok')

