from flask import Flask, render_template, request
import config
import csv
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)


@app.route("/")
def index():
    account = client.get_account()

    balances = account['balances']
    # print(balances)

    exchange_info = client.get_exchange_info()
  #  print(exchange_info)
    symbols = exchange_info['symbols']

    return render_template("index.html", my_balances= balances, symbols= symbols)


@app.route("/Buy", methods=['POST'])
def Buy():
        print(request.form)
        order = client.create_order(
        symbol=request.form['symbol'],
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=request.form['quantity'])

        return "Buy"


@app.route("/Sell")
def Sell():
    return "Sell"


@app.route("/Settings")
def Settings():
    return "Settings"
