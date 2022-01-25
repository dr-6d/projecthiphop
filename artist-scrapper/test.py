from selenium import webdriver
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
url= "https://www.billboard.com/charts/year-end/2010/hot-rap-songs/"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
officials = soup.findAll("div",{"class":"o-chart-results-list-row-container"})

for entry in officials:
    print(str(entry.find('h3')))


driver.quit()