from http.client import responses
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

class GetPriceFromId:
    """Gets data through buff api for a given item Id"""

    def __init__(self, id ):
        self.id = id
        self.url = 'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id='+str(id)+'&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_=1668881309653'
        self.headers = {"Accept-Language": "fr,en-US;q=0.9,en;q=0.8"}

        self.res = requests.get(url=self.url, headers = self.headers).json()

    def getName(self):
        return self.res['data']['goods_infos'][str(self.id)]['name']
        
    def getLowestPrice(self):
        return self.res['data']['items'][0]['price']

"""
    def getStickers(self):
        """useless function in that case, see Sticker class"""
        return self.res['data']['items'][]
"""