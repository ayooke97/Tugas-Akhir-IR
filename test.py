import lxml
import requests
from bs4 import BeautifulSoup


url = 'https://animeisme.me/rilis/2021'

html = requests.get(url).text


soup = BeautifulSoup(html, 'lxml')

test = soup.select("span title")


anime_name = soup.find_all('h2', itemprop= 'name')

anime_name_after = (BeautifulSoup(str(anime_name[0]),'lxml').get_text().strip('[]'))

print(anime_name_after.replace('2021',''))
rating = soup.find_all('span', class_= 'rating')


for i in range (0,len(anime_name)- 10):
    print(str(i + 1) + ". ", end= '')
    print("Nama Anime : " ,BeautifulSoup(str(anime_name[i]),'lxml').get_text().strip('[]').replace('2021',''))
    print("    Rating :",BeautifulSoup(str(rating[i]),'lxml').get_text().strip('[]').replace('RATING',''))











































