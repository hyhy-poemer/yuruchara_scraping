import requests
import re
from bs4 import BeautifulSoup

def rank_year(year):
    """
     各年度のランキングのリンクを取得
     """

    url = "http://www.yurugp.jp/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    link = soup.find('a', href = 'http://www.yurugp.jp/ranking/?year=' + str(year))

    return(link.get('href'))

def get_images():

    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

    for year in years:
        rank_link = rank_year(year)
        response  = requests.get(rank_link)


