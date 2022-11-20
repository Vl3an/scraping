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
            self.itemList.append( requests.get(url=self.url, headers = self.headers).json()['data'] )


    def getUrl(id,nb) -> str:
        return "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id="+str(id)+"&page_num="+str(nb)+"&sort_by=default&mode=&allow_tradable_cooldown=1&extra_tag_ids=squad_combos&wearless_sticker=1&_=1668903032399"

    def 




