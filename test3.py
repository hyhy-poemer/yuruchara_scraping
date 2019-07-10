# 画像のスクレイピングはできたが解像度が 110x134
import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.yurugp.jp/ranking/?year=2018'
# PATH = './Users/hyhy/Documents/YURUCHARA_GANs/Scraping/scraping_env/IMG'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all('img', src=re.compile(
    '^http://www.yurugp.jp/img/uploads/character'))
for link in links:
    print(link['src'])

    r = requests.get(link['src'])
    with open('img/' + link['src'].split('/')[-1], 'wb') as file:
        file.write(r.content)
