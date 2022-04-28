import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#   print(price)

candles = client.get_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_5MINUTE)

csvfile = open('ETHUSDT_2021-2022.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

#print(len(candles))

#for candlestick in candles:
 #   print(candlestick)
  #  candlestick_writer.writerow(candlestick)

candlesticks = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2021", " 1 Jan, 2022")

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close()

