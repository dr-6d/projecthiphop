from bs4 import BeautifulSoup
import requests



page = requests.get("https://beats-rhymes-lists.com/lists/top-30-best-rappers-of-the-2010s/")
print(page)


soup = BeautifulSoup(page.content, 'html.parser')

soup = soup.find_all('h2')

artistList = []

for i in range(len(soup)):
    # print(str(i) + " :- " + str(soup[i].contents))
    if (i <= 32 and i>=3):
        artistList.append(soup[i].contents)

del soup, page

# print(artistList)


cleanList = []

for i in range(len(artistList)):
    if i< 21:
        artist = artistList[i][0][4:]
        cleanList.append(artist)
    else : 
        artist = artistList[i][0][3:]
        cleanList.append(artist)

print(len(cleanList))