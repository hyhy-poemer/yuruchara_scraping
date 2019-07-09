import requests
import re
from bs4 import BeautifulSoup

session = requests.Session()

def main():
    """  
    クローラーのメイン処理
    """
    # ゆるキャラグランプリの HP
    url = "http://www.yurugp.jp/"

    r = session.get(url)
    soup = BeautifulSoup(r)
    links = soup.find_all('a', href=re.compile(r'http://www.yurugp.jp/ranking/\?year=20\d{2}')) #2011~2018 年のランキングの url を抽出
    rank_img_urls = rank_year(links)

    for rank_img_url in rank_img_urls:
        s = get_img_url(rank_img_url)
        response = requests.get(s['src'])
        with open('img/'+s['src'].split('/')[-1],'wb') as file:
            file.write(response.content)

def rank_year(links):
    """
    ランキングページから画像の url を抽出する
    """
    session = requests.Session()

    for link in links:
        link = link.get('href')
        r = session.get('link')
        soup = BeautifulSoup(r)
        urls = soup.find_all('a', href=re.compile(r'http://www.yurugp.jp/vote/detail.php?id=\d{8}'))
    
    return urls

def get_img_url(link):
    """
     ゆるキャラ個別のページから画像をソースを抽出
    """
    img_url = link.get('href')
    img_r = requests.get('img_url')
    soup = BeautifulSoup(img_r)
    img_url = soup.find('img', src=re.compile('^http://www.yurugp.jp/img/uploads/character/650'))

    return img_url

if __name__ == '__main__':
    main()