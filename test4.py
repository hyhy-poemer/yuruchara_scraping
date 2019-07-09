#  各年のゆるキャラランキングページから全順位分のページを引っ張ってこれるかテスト

import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.yurugp.jp/ranking/?year=2018'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
rank_links = soup.find_all('option', value=re.compile(r'rank=\d+_\d{3}&year=20\d{2}'))
rank_links_unique = list(set(rank_links))

for link in rank_links_unique:
    print(link.get('value'))




# i = 0
# for link in rank_links:
#     if i == 3:
#         break
#     else:
#         a = link.get('value')
#         print('http://www.yurugp.jp/ranking/'+str(a))
#         i+=1



