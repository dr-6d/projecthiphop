from bs4 import BeautifulSoup
import requests



page = requests.get("https://loudbeats.org/hip-hop/best-rappers/")
print(page)


soup = BeautifulSoup(page.content, 'html.parser')

soup = soup.find('ul', class_="ez-toc-list ez-toc-list-level-1")
soup = soup.find_all('a')

cleanList = []

for i in range(len(soup)):
    if i < 10:
        artist = soup[i].contents[0][3:]
    else:
        artist = soup[i].contents[0][4:]
    cleanList.append(artist)
print(cleanList)