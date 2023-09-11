import json
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.76"
}


start_num = 6872580
end_num = 6872600
# end_num = 6872599

output_file = "book_list.json"  

for num in range(start_num, start_num + 1):
    url = f"https://book.douban.com/subject/{num}"
    response = requests.get(url=url,headers=headers)
    html_content = response.text
    
    soup = BeautifulSoup(html_content, "html.parser")
    print(html_content)
    title = soup.find("h1")
    print(title)
    title = title.find("span")
    book_list =[]
    intro = soup.find("div", attrs={"class": "intro"})
    if intro==None:
        print("暂无简介")
    else:
        print(intro)
    iii = {"title": title, "简介": intro}  
    print(title)
    book_list.append(iii)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(book_list, f, ensure_ascii=False)

print(f"书目信息已保存到 {output_file} 文件中。")