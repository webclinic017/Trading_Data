import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#   print(price)

candles = client.get_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_5MINUTE)

csvfile = open('5minutes.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

print(len(candles))

for candlestick in candles:
    print(candlestick)
    candlestick_writer.writerow(candlestick)
