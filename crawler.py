from bs4 import BeautifulSoup
import requests
import json
with open("thirukkural.json") as data:
    content = json.load(data)

thirukkural = open("thirukkural.txt","w+")

for kuralkal in content["kural"]:
    thirukkural.write(kuralkal["Line1"]+"\n")
    thirukkural.write(kuralkal["Line2"] + "\n")

thirukkural.close()
print( "File created !")