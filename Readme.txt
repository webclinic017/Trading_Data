Binance App

Using websockets and real time light weight charts

wscat- connect to websocket from the command line
stream - wss://stream.binance.com:9443/ws/ethusdt@trade
wss://stream.binance.com:9443/ws/ethusdt@kline_5m

{"e":"trade","E":1651074259668,"s":"ETHUSDT","t":811140471,"p":"2863.50000000","q":"1.34580000","b":8716559444,"a":8716559507,"T":1651074259667,"m":true,"M":true}

{"e":"kline","E":1651074573997,"s":"ETHUSDT","k":{"t":1651074300000,"T":1651074599999,"s":"ETHUSDT","i":"5m","f":811140720,"L":811143339,"o":"2863.33000000","c":"2867.10000000","h":"2872.36000000","l":"2861.09000000","v":"1944.44130000","n":2620,"x":false,"q":"5575689.67424900","V":"1036.68130000","Q":"2972452.83363100","B":"0"}}

capture output to a file
connect to websocket from the web / javascript
lightweight charts-  create real time candlestick chart similiar to tradingview
UI to check indicators (eg RSI, EMA,SMA)


Technical analysis with python and TA-Lib

connect to websockets from python, write candlestick data to csv
download historical data using a REST API
using TA-Lib, try some indicators

Back testing with TA-Lib and Backtrader

test some indicators against a historical dataset
plot some charts

building an APT for indicator settings

API endpoint to save/persist indicators
using setting from python websockets
API endpoint for executing a buy order
API endpoint for sending notification

Add stuff to UI