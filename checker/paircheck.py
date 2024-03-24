import requests

class all_symb():
    def all_symb():
        infourl = 'https://api.bybit.com/v5/market/tickers?category=spot'
        req = requests.get(infourl).json()
        return req


class bybite():
    # Название биржи
    se = 'bybite'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.bybit.com/trade/spot/{crypt1}/{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.bybit.com/v5/market/tickers?category=spot&symbol={crypt1}{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['result']['list'][0]['lastPrice']
        except:
            price = 0
        return price

class okx():
    # Название биржи
    se = 'okx'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.okx.com/ru/trade-spot/{crypt1}-{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://www.okx.com/api/v5/market/index-tickers?instId={crypt1}-{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['data'][0]['idxPx']
        except:
            price = 0
        return price

class commex():
    # Название биржи
    se = 'commex'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.commex.com/en/trade/{crypt1}_{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.commex.com/api/v1/ticker/price?symbol={crypt1}{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price1 = float(requests.get(url).json()['price'])
            price = str(round(price1, 2))
        except:
            price = 0
        return price

class coinbase():
    # Название биржи
    se = 'coinbase'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://pro.coinbase.com/trade/{crypt1}-{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.exchange.coinbase.com/products/{crypt1}-{crypt2}/ticker'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['price']
        except:
            price = 0
        return price

class cryptocom():
    # Название биржи
    se = 'cryptocom'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://crypto.com/exchange/trade/{crypt1}_{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.crypto.com/v2/public/get-ticker?instrument_name={crypt1}_{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['result']['data'][0]['a']
        except:
            price = 0
        return price

class bitget():
    # Название биржи
    se = 'bitget'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.bitget.com/ru/spot/{crypt1}{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.bitget.com/api/v2/spot/market/tickers?symbol={crypt1}{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['data'][0]['lastPr']
        except:
            price = 0
        return price

class kucoin():
    # Название биржи
    se = 'kucoin'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.kucoin.com/ru/trade/{crypt1}-{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={crypt1}-{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['data']['price']
        except:
            price = 0
        return price

class htx():
    # Название биржи
    se = 'htx'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        cryp1 = str(crypt1).lower()
        cryp2 = str(crypt2).lower()
        url = f'https://www.htx.com/ru-ru/trade/{cryp1}_{cryp2}?type=spot'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        cryp1 = str(crypt1).lower()
        cryp2 = str(crypt2).lower()
        url_api = f'https://api.huobi.pro/market/detail/merged?symbol={cryp1}{cryp2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['tick']['close']
        except:
            price = 0
        return price

class gateio():
    # Название биржи
    se = 'gateio'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.gate.io/ru/trade/{crypt1}_{crypt2}'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.gateio.ws/api/v4/spot/tickers?currency_pair={crypt1}_{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()[0]['last']
        except:
            price = 0
        return price

class bingx():
    # Название биржи
    se = 'bingx'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://bingx.com/ru-ru/spot/{crypt1}{crypt2}/'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://open-api.bingx.com/openApi/spot/v1/ticker/24hr?timestamp=0&symbol={crypt1}-{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['data'][0]['lastPrice']
        except:
            price = 0
        return price

class mexc():
    # Название биржи
    se = 'mexc'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.mexc.com/ru-RU/exchange/{crypt1}_{crypt2}/'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api.mexc.com/api/v3/ticker/price?symbol={crypt1}{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['price']
        except:
            price = 0
        return price

class exmo():
    # Название биржи
    se = 'exmo'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://exmo.me/trade/pro/{crypt1}_{crypt2}/'
        return url

    # Генерируем урл на апи
    def apiurl(self):
        url_api = f'https://api.exmo.me/v1.1/ticker'
        return url_api

    # Получаем прайс на пару
    def price(url, crypt1, crypt2):
        try:
            price = requests.get(url).json()[f'{crypt1}_{crypt2}']['last_trade']
        except:
            price = 0
        return price

class bitmart():
    # Название биржи
    se = 'bitmart'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.bitmart.com/trade/en-US?symbol={crypt1}_{crypt2}/'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        url_api = f'https://api-cloud.bitmart.com/spot/quotation/v3/ticker?symbol={crypt1}_{crypt2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['data']['last']
        except:
            price = 0
        return price

class digifinex():
    # Название биржи
    se = 'digifinex'

    # Преобразуем валюты в пары
    def pair(crypt1, crypt2):
        pair = f'{crypt1}-{crypt2}'
        return pair

    # Генерируем урл на торговлю
    def url(crypt1, crypt2):
        url = f'https://www.digifinex.com/en-ww/trade/{crypt1}/{crypt2}/'
        return url

    # Генерируем урл на апи
    def apiurl(crypt1, crypt2):
        cryp1 = str(crypt1).lower()
        cryp2 = str(crypt2).lower()
        url_api = f'https://openapi.digifinex.com/v3/ticker?symbol={cryp1}_{cryp2}'
        return url_api

    # Получаем прайс на пару
    def price(url):
        try:
            price = requests.get(url).json()['ticker'][0]['sell']
        except:
            price = 0
        return price