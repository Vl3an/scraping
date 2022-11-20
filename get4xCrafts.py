from http.client import responses
from multiprocessing.spawn import import_main_path
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import parameters

class Get4xCrafts:

    def __init__(self,id,nb) -> None:
        self.id = id
        self.nb = nb

        self.itemList = []
        self.headers = parameters.headers

        for i in range(nb):
            print(Get4xCrafts.getUrl(id,i))
            r = requests.get(Get4xCrafts.getUrl(id,i), headers = self.headers).json()

            for itemIndex in range(10):
                if r['code'] == "OK":
                    self.itemList.append( r['data']['items'][itemIndex] )
                else: 
                    print("request error for item id"+str(id)+" at page "+str(i+1)+" : error code "+r['code'])

    def getStickerPrice(name : str):
        ###TODO 
        """get the sticker corresponding id via database"""
        pass

    def getStickerNames(self) -> list[str]:
        stickerNames = []

        for item in self.itemList:
            itemStickers = []
            for sticker in item['asset_info']['info']['stickers']:
                itemStickers.append(sticker['name'])
            stickerNames.append(itemStickers)
        return stickerNames

    def getUrl(id : int,nb : int) -> str:
        return "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id="+str(id)+"&page_num="+str(nb+1)+"&sort_by=default&mode=&allow_tradable_cooldown=1&extra_tag_ids=squad_combos&wearless_sticker=1&_=1668942549595"





