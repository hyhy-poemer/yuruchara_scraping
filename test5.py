import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.yurugp.jp/ranking/?rank=1_200&year=2018'

response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
img_urls = soup.find_all('a', href=re.compile(r'../character/detail.php\?id=\d{8}'))
print(img_urls)
for url in img_urls:
    print(url.get('href'))