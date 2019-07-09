import requests
import re
from bs4 import BeautifulSoup

url = "http://www.yurugp.jp/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

links = soup.find_all('a', href=re.compile(r'http://www.yurugp.jp/ranking/\?year=20\d{2}'))
print(links)
for link in links:
   print(link.get('href'))