"""
かくゆるキャラが持つ個別ページから，最大の解像度の画像を抽出
"""

import re

from bs4 import BeautifulSoup

import requests

url = 'http://www.yurugp.jp/character/detail.php?id=00000889'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link = soup.find('img', src=re.compile(
    r'^http://www.yurugp.jp/img/uploads/character/650/\d{8}.jpg'))

# print(link.get('src'))
res = requests.get(link['src'])
with open('img/' + link['src'].split('/')[-1], 'wb') as file:
    file.write(res.content)
