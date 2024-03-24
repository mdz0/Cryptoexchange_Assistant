Поддерживаемые на данных момент биржи: bybite, okx, commex, coinbase, bitget, kucoin, htx, gateio, bingx, mexc, exmo, bitmart, digifinex 

Скачиваем
Устанавливаем зависимости requirements.txt
Запускаем через main.py
Переходим на главную страницу - http://localhost:5438/ , находим нужную пару
Вбиваем http://localhost:5438/check/{Нужная пара}, например http://localhost:5438/check/BTC-USDT, обязательно вбиваем пару через '-'
Если пара не торгуется на конкретной бирже, в графе 'price' будет 0
