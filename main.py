from pickle import GET
import GetPriceFromId
import Get4xCrafts
import time
getPriceOfM4 = GetPriceFromId.GetPriceFromId(35282)
#getPriceTest = GetPriceFromId.GetPriceFromId(35383)

#print(getPriceOfM4.getName(), getPriceTest.getName())

#print(getPriceOfM4.getLowestPrice(), getPriceTest.getLowestPrice())

print(getPriceOfM4.getStickerNames())



getM4crafts = Get4xCrafts.Get4xCrafts(35282,1)

print(getM4crafts.getStickerNames())