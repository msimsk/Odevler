import requests


class Euro:
    prices = []

    def __init__(self, sell):
        self.prices.append(sell)

    def goster():
        print("EUR" + str(Euro.prices))


class CADollar:
    prices = []

    def __init__(self, sell):
        self.prices.append(sell)

    def goster():
        print("CAD:" + str(CADollar.prices))

class USDollar:
    prices = []

    def __init__(self, sell):
        self.prices.append(sell)

    def goster():
         print("USD:" + str(USDollar.prices))

class Factory:
    def setCrypto(self, cryptoName, sell):
        if cryptoName == 'EUR':
            Euro(sell)
        elif cryptoName == 'CAD':
            CADollar(sell)
        elif cryptoName == 'USD':
            USDollar(sell)


class Goster:
    def factory(many):
        if many == 'EUR':
            Euro.goster()
        elif many == 'CAD':
            CADollar.goster()
        elif many == 'USD':
            USDollar.goster()
        else:
            print(many + " verisi bulunmamaktadır!!!")




factory = Factory()
istek = requests.get("https://blockchain.info/ticker").json()

for i in istek:
    factory.setCrypto(i, str(istek[i]["sell"]))

liste = ["CHF","USD","CAD","EUR","TRY"]

for i in liste:
    Goster.factory(i)

