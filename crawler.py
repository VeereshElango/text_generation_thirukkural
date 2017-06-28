from bs4 import BeautifulSoup
import requests

thirukural = open("thirukural.txt","w+")
total_chapters = 1330
for i in range(1, total_chapters):
    page = "0"*(4-len(str(i))) + str(i)
    if i ==1 or i==2:
        page= page+"_16"
    url = "http://agaram-thirukkural.blogspot.fr/2009/04/"+page+".html"
    # print(index+1, i)
    print("Crawling url :" + url)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, )

    #print(kural)
    try:
        kural = soup.find_all('div', {"class": "right"})[4]
        for line in str(kural).split('<div class="right">')[1].split('</div>')[0].split("<br/>"):
            thirukural.write(line)
    except :
        print (page +"Notworking")



thirukural.close()

# # print("Total words : ", len(ponniyin_selvan))
# url = "http://agaram-thirukkural.blogspot.fr/2009/04/1330.html"
# #print(index+1, i)
# print("Crawling url :"+url )
# r  = requests.get(url)
# data = r.text
# soup = BeautifulSoup(data,)
# kural = soup.find_all('div',{"class":"right"})[4]
# print(str(kural).split('<div class="right">')[1].split('</div>')[0].split("<br/>"))

