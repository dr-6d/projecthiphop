from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.highsnobiety.com/p/rappers-real-names/")
print(page)

soup = BeautifulSoup(page.content, 'html.parser')

soup = soup.find('div', class_="contentWrapper___NsYuy")
soup = soup.find_all('h4')

cleanList = []

for i in soup:
    cleanList.append(i.span.contents[0])

print(cleanList)