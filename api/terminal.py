import os
import requests
import pandas as pd
import time, json
from time import sleep
import auth
import keys
import string, random
import postOrder as po


def takeInput():
    inp = input('Limit or Market? (l/m): ')
    if inp == 'l':
        market = input('Market: ')
        side = input('Side (s/b): ')
        price = float(input('Price: '))
        size = float(input('Size: '))
        if side == 's':
            po.placeLimitOrder(market, 'sell', price, size)
            print("SELL Limit Order Placed!")
        elif side == 'b':
            po.placeLimitOrder(market, 'buy', price, size)
            print("BUY Limit Order Placed!")
        else:
            print('Invalid side')
        # po.placeLimitOrder(market, side, price, size)
    if inp == 'm':
        market = input('Market: ')
        side = input('Side (s/b): ')
        size = float(input('Size: '))
        if side == 's':
            po.placeMarketOrder(market, 'sell', size)
            print("SELL Limit Order Placed!")
        elif side == 'b':
            po.placeMarketOrder(market, 'buy', size)
            print("BUY Market Order Placed!")
        else:
            print('Invalid side')
        # po.placeMarketOrder(market, side, size)
    else:
        print('Invalid input')
    # return po.placeLimitOrder(str(market), str(side), float(price), float(size))

takeInput()