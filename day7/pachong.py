from bs4 import BeautifulSoup
import requests
import json
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.5162 SLBChan/111"
}
num=6872578
x=0
lis=[]
for i in range(30):
    content=requests.get(f"https://book.douban.com/subject/{num+i}/",headers=headers).text

    soup=BeautifulSoup(content,"html.parser")
    x+=1

    title=soup.find("h1")
    title=title.find("span")
    intro=soup.find("div",attrs={"class":"intro"})

    if intro==None:
        intro_all="暂无简介"
    else:
        intro_all=""
        intro=intro.find_all("p")
        for intro_every in intro:
            intro_all+=intro_every.string
    lis.append({"book_name":title.string,"introduction":intro_all})
    

with open('./douban.json','w',encoding='utf-8') as fp:
     json.dump(lis , fp,ensure_ascii=False,indent=4,sort_keys=True)
     print('ok')

