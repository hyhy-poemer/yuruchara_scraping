import lxml.html
from urllib.request import urlopen

tree = lxml.html.parse(urlopen('http://www.yurugp.jp/ranking/?year=2018'))
html = tree.getroot()

for a in html.cssselect('a'):
    print(a.get('href'),a.text)