import json
import  urllib.request as url

class Currency:
    def __init__(self):
        self.alisFiyati = None
        self.satisFiyati = None

    def getAlisFiyati(self):
        return self.alisFiyati
    def getSatisFiyati(self):
        return self.satisFiyati



class USD(Currency):
    def __init__(self,alisFiyati,satisFiyati):
        print(f"1 BTC Dolar olarak Alış Fiyatı:{alisFiyati}$ Satış Fiyatı:{satisFiyati}$")
class PLN(Currency):
    def __init__(self,alisFiyati,satisFiyati):
        print(f"1 BTC Polonya Zlotisi olarak Alış Fiyatı:{alisFiyati}zł Satış Fiyatı:{satisFiyati}zł")
class EUR(Currency):
    def __init__(self, alisFiyati, satisFiyati):
        print(f"1 BTC Euro olarak Alış Fiyatı:{alisFiyati}€ Satış Fiyatı:{satisFiyati}€")

class Factory:
    def getCurrency(self,k,veri):
       if k == "USD":
          return USD(veri['buy'],veri['sell'])
       if k == "PLN":
          return PLN(veri['buy'], veri['sell'])
       if k == "EUR":
           return EUR(veri['buy'], veri['sell'])




jsonurl = url.urlopen("https://blockchain.info/ticker")
veri = json.load(jsonurl)

factory = Factory()

for k,v in veri.items():
    factory.getCurrency(k,v)

