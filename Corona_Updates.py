import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div", class_ = "maincounter-number" )

print("Total de Casos Confirmados : ", data[0].text.strip())
print("Total de Mortos : ", data[1].text.strip())
print("Total de Recuperados : ", data[2].text.strip())