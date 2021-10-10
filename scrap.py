import requests
from bs4 import BeautifulSoup as bs
import csv

def a():
    url = "https://otakudesu.moe/anime-list/#"
    req = requests.get(url).text
    soup = bs(req, "html.parser")
    #print(soup.prettify())
    write = csv.writer(open("otakudesu_animlist.csv", "w"))
    head = ["Anime List"]
    write.writerow(head)
    return soup
    
def s():
    ok = a()
    dat = []
    cari = ok.find_all("div","jdlbar")
    for car in cari:
        name = car.find("a","hodebgst").text
        dat.append([name])
    return dat
    
def main():
    ok = s()
    count=0
    for i in ok:
        write = csv.writer(open("otakudesu_animlist.csv", "a", newline=""))
        write.writerow(i)
        count+=1
        print(count,i)
        
if __name__ == "__main__":
    main()
