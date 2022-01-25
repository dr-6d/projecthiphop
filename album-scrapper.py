
from bs4 import BeautifulSoup
import requests



baseURL = "https://www.discogs.com"
page = requests.get(baseURL +  "/search/?q=" + "drake" + "&type=all")
print(page)


soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find('a', class_="thumbnail_link")
# soup = soup.find('img')
# 
artistURL = baseURL + soup['href']
artistPage =requests.get('https://www.discogs.com/artist/151199-Drake?type=Releases&subtype=Albums&filter_anv=0')

# print(artistPage)


artistSoup = BeautifulSoup(artistPage.content, 'html.parser')
artistSoup = artistSoup.find_all('td', class_='title')
for i in artistSoup:
    print(i.a.contents)