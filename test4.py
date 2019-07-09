import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.yurugp.jp/vote/detail.php?id=00000364'
r = requests.get(url)
