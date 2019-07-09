import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

session = requests.Session()

def main():
    """  
    クローラーのメイン処理，画像を保存
    """
    # ゆるキャラグランプリの HP
    url = "http://www.yurugp.jp/"

    r = session.get(url)
    soup = BeautifulSoup(r)
    links = soup.find_all('a', href=re.compile(r'http://www.yurugp.jp/ranking/\?year=20\d{2}')) #2011~2018 年のランキングの url を抽出
    img_urls = rank_year(links)


    for img_url in img_urls:
        img_url = img_url.get('href')
        img_url_join = urljoin('http://www.yurugp.jp/',url)
        s = get_img_url(img_url_join)
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
        r = session.get(link)
        soup = BeautifulSoup(r)
        rank_links = soup.find_all('option', value=re.compile(r'rank=\d+_\d{3}&year=20\d{2}'))
        rank_links_unique = list(set(rank_links)) #重複を削除

        for rank_link in rank_links_unique:
            response = session.get('http://www.yurugp.jp/ranking/'+str(rank_link))
            img_soup = BeautifulSoup(response)
            img_urls = img_soup.find_all('a', href=re.compile(r'../character/detail.php\?id=\d{8}'))

    return img_urls

def get_img_url(link):
    """
     ゆるキャラ個別のページから画像のソースを抽出
    """
    img_url = link.get('href')
    img_r = requests.get(img_url)
    soup = BeautifulSoup(img_r)
    img_url = soup.find('img', src=re.compile('^http://www.yurugp.jp/img/uploads/character/650'))

    return img_url

if __name__ == '__main__':
    main()