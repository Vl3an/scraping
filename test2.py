from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


url = "https://buff.163.com/goods/35282#tab=selling"
headers = {"Accept-Language": "fr,en-US;q=0.9,en;q=0.8"}


response = requests.get(url, headers)

soup = BeautifulSoup(response.text, "html.parser")
title = soup.find('title')
print(title)


res = requests.get('https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=35282&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_=1668881309653').json()

for price in res['data']['items']:
    print(price['price'])
    print(price['user_id'])




trs = soup.findAll('strong')
print(len(trs))

print(trs[0])

#print(soup)

#"<div style=\"display: table-cell;\">\n.*<strong class=\"f_Strong\">¥ "