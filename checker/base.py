from checker.paircheck import *


class check():


    def bybit(self, cryp1, cryp2):
        basese = bybite  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def okx(self, cryp1, cryp2):
        basese = okx  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def commex(self, cryp1, cryp2):
        basese = commex  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def coinbase(self, cryp1, cryp2):
        basese = coinbase  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def cryptocom(self, cryp1, cryp2):
        basese = cryptocom  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def bitget(self, cryp1, cryp2):
        basese = bitget  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def kucoin(self, cryp1, cryp2):
        basese = kucoin  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def htx(self, cryp1, cryp2):
        basese = htx  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def gateio(self, cryp1, cryp2):
        basese = gateio  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def bingx(self, cryp1, cryp2):
        basese = bingx  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def mexc(self, cryp1, cryp2):
        basese = mexc  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def exmo(self, cryp1, cryp2):
        basese = exmo  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(object)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl, cryp1, cryp2)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def bitmart(self, cryp1, cryp2):
        basese = bitmart  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

    def digifinex(self, cryp1, cryp2):
        basese = digifinex  # Название биржи

        pair = basese.pair(cryp1, cryp2)  # Преобразуем валюты в пару
        seurl = basese.url(cryp1, cryp2)  # Генерируем нужный урл для быстрой ссылки на биржу на пару
        apiurl = basese.apiurl(cryp1, cryp2)  # Генерируем ссылку на апи биржи для запроса
        price = basese.price(apiurl)  # Получаем прайс на пару
        se = basese.se  # Возвращаем название биржи
        return se, cryp1, cryp2, pair, price, seurl, apiurl  # Передаем данные дальше

# Посылаем словарь на апи
class check_return():
    def check_return(cryp1, cryp2):

        pair = check # Класс пары

        bybite = pair.bybit(object, cryp1, cryp2)
        okx = pair.okx(object, cryp1, cryp2)
        commex = pair.commex(object, cryp1, cryp2)
        coinbase = pair.coinbase(object, cryp1, cryp2)
        bitget = pair.bitget(object, cryp1, cryp2)
        kucoin = pair.kucoin(object, cryp1, cryp2)
        htx = pair.htx(object, cryp1, cryp2)
        gateio = pair.gateio(object, cryp1, cryp2)
        bingx = pair.bingx(object, cryp1, cryp2)
        mexc = pair.mexc(object, cryp1, cryp2)
        exmo = pair.exmo(object, cryp1, cryp2)
        bitmart = pair.bitmart(object, cryp1, cryp2)
        digifinex = pair.digifinex(object, cryp1, cryp2)

        bybite_msg = {
            "name": f"{bybite[0]}",
            "price": f"{bybite[4]}",
            "se_url": f"{bybite[5]}",
        }
        okx_msg = {
            "name": f"{okx[0]}",
            "price": f"{okx[4]}",
            "se_url": f"{okx[5]}",
        }
        commex_msg = {
            "name": f"{commex[0]}",
            "price": f"{commex[4]}",
            "se_url": f"{commex[5]}",
        }
        coinbase_msg = {
            "name": f"{coinbase[0]}",
            "price": f"{coinbase[4]}",
            "se_url": f"{coinbase[5]}",
        }
        bitget_msg = {
            "name": f"{bitget[0]}",
            "price": f"{bitget[4]}",
            "se_url": f"{bitget[5]}",
        }
        kucoin_msg = {
            "name": f"{kucoin[0]}",
            "price": f"{kucoin[4]}",
            "se_url": f"{kucoin[5]}",
        }
        htx_msg = {
            "name": f"{htx[0]}",
            "price": f"{htx[4]}",
            "se_url": f"{htx[5]}",
        }
        gateio_msg = {
            "name": f"{gateio[0]}",
            "price": f"{gateio[4]}",
            "se_url": f"{gateio[5]}",
        }
        bingx_msg = {
            "name": f"{bingx[0]}",
            "price": f"{bingx[4]}",
            "se_url": f"{bingx[5]}",
        }
        mexc_msg = {
            "name": f"{mexc[0]}",
            "price": f"{mexc[4]}",
            "se_url": f"{mexc[5]}",
        }
        exmo_msg = {
            "name": f"{exmo[0]}",
            "price": f"{exmo[4]}",
            "se_url": f"{exmo[5]}",
        }
        bitmart_msg = {
            "name": f"{bitmart[0]}",
            "price": f"{bitmart[4]}",
            "se_url": f"{bitmart[5]}",
        }
        digifinex_msg = {
            "name": f"{digifinex[0]}",
            "price": f"{digifinex[4]}",
            "se_url": f"{digifinex[5]}",
        }

        all_se_msg = [
            bybite_msg,
            okx_msg,
            commex_msg,
            coinbase_msg,
            bitget_msg,
            kucoin_msg,
            htx_msg,
            gateio_msg,
            bingx_msg,
            mexc_msg,
            exmo_msg,
            bitmart_msg,
            digifinex_msg,
        ]

        json_msg = {
            'pair': f'{cryp1}-{cryp2}',
            'cry1': f'{cryp1}',
            'cry2': f'{cryp2}',
            'se_price': all_se_msg
        }

        return json_msg



