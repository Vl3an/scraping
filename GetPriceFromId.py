from http.client import responses
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

class GetPriceFromId:
    """Gets data through buff api for a given item Id, used to get lowest price"""

    def __init__(self, id ) -> None:
        self.id = id
        self.url = 'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id='+str(id)+'&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_=1668881309653'
        self.headers = {"Accept-Language": "fr,en-US;q=0.9,en;q=0.8"}

        self.res = requests.get(url=self.url, headers = self.headers).json()

    def getName(self) -> str:
        return self.res['data']['goods_infos'][str(self.id)]['name']
        
    def getLowestPrice(self) -> float:
        return self.res['data']['items'][0]['price']

    #no use

    def getSticker(self):
        """useless function in that case, see Sticker class"""

        return [item['asset_info']['info']['stickers'] for item in self.res['data']['items']]

    def getStickerNames(self):
        stickerNames = []

        for item in self.res['data']['items']:
            itemStickers = []
            for sticker in item['asset_info']['info']['stickers']:
                    itemStickers.append(sticker['name'])
            stickerNames.append(itemStickers)
        return stickerNames


            

                

