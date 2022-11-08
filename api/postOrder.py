import os
import requests
import pandas as pd
import time, json
from time import sleep
import auth
import keys
import string, random

api_key = keys.api_key
api_secret = keys.api_secret

c = auth.FtxClient(api_key=api_key, api_secret=api_secret)

def get_price(market:str):
    try:
        market_data = requests.get('https://ftx.com/api/markets/%s' % market).json()
        price = market_data['result']['price']
        return price
    except Exception as e:
        print(f'Error obtaining BTC data: {e}')

# Places a limit order
def placeLimitOrder(market:str, side:str, price:float, size:float):
    client_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    try:
        order = c.place_order(market=market, side=side, price=price, size=size, client_id=client_id)
        print(order)
    except Exception as e:
        print(f'Error: {e}')
    sleep(2)

# Places a market order
def placeMarketOrder(market:str, side:str, size:float):
    client_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    mktPrice = get_price(str(market))
    try:
        order = c.place_order(market=market, side=side, price=mktPrice, size=size, client_id=client_id)
        print(order)
    except Exception as e:
        print(f'Error: {e}')
    sleep(2)


## placeLimitOrder('BTC-PERP', 'buy', 20000, 0.0001)
