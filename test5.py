"""
ランキングページから各ゆるキャラへのリンクは相対 url なので，これを絶対 url に変換
"""

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

import requests


url = 'http://www.yurugp.jp/ranking/?rank=1_200&year=2018'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
img_urls = soup.find_all('a', href=re.compile(
    r'../character/detail.php\?id=\d{8}'))
print(img_urls)
for url in img_urls:
    url = url.get('href')
    abs_url = urljoin('http://www.yurugp.jp/', url)
    print(abs_url)
