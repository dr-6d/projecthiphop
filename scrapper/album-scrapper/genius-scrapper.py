from bs4 import BeautifulSoup
import requests



page = requests.get("https://genius.com/artists/Kendrick-lamar")
print(page)


soup = BeautifulSoup(page.content, 'html.parser')




soup = soup.find('div', {"ng-if":"$scrollable_data_ctrl.models.length"})

# soup = soup.find('div', class_="thumbnail_grid white_container")

# soup = soup.find_all('h3')

albumList = []

for i in range(len(soup)):
    print(soup[i].contents)