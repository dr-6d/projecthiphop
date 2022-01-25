
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.billboard.com/charts/year-end/2010/hot-rap-songs/")
print(page)

soup = BeautifulSoup(page.content, 'html.parser')

soup = soup.find_all('div', class_="o-chart-results-list-row-container")

cleanList = []

for i in soup:
    song = str(i.find('h3').innerText)
    # cleanList.append(i.span.contents[0])
    print(song)

# print(cleanList)