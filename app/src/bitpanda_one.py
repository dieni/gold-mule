from calendar import c
import os
import pandas
import time
from predict import predict_ltc
from models import Observation
from datetime import datetime
import http.client
import json

PERIOD = 'm1'
ROWS = 2
ASSETS = ['BTC/USD', 'BCH/USD', 'ETH/USD', 'LTC/USD', 'XRP/USD', 'EOS/USD', 'XLM/USD']
# is_active = False

def get_observation(con):


    res = con.getresponse()
    data = res.read()

    data = json.loads(data)
    # print(json.dumps(data, indent=2, sort_keys=True))
    
    print(f"THE TIME IS: {data[0]['time']}")

    observation = Observation(
        BTC=float([d['last_price'] for d in data if d['instrument_code'] == 'BTC_EUR'][0]), 
        BCH=float([d['last_price'] for d in data if d['instrument_code'] == 'BCH_EUR'][0]), 
        ETH=float([d['last_price'] for d in data if d['instrument_code'] == 'ETH_EUR'][0]), 
        LTC=float([d['last_price'] for d in data if d['instrument_code'] == 'LTC_EUR'][0]), 
        XRP=float([d['last_price'] for d in data if d['instrument_code'] == 'XRP_EUR'][0]), 
        EOS=float([d['last_price'] for d in data if d['instrument_code'] == 'EOS_EUR'][0]), 
        XLM=float([d['last_price'] for d in data if d['instrument_code'] == 'XLM_EUR'][0]),
        dBTC=float([d['price_change'] for d in data if d['instrument_code'] == 'BTC_EUR'][0]), 
        dBCH=float([d['price_change'] for d in data if d['instrument_code'] == 'BCH_EUR'][0]), 
        dETH=float([d['price_change'] for d in data if d['instrument_code'] == 'ETH_EUR'][0]), 
        dLTC=float([d['price_change'] for d in data if d['instrument_code'] == 'LTC_EUR'][0]), 
        dXRP=float([d['price_change'] for d in data if d['instrument_code'] == 'XRP_EUR'][0]), 
        dEOS=float([d['price_change'] for d in data if d['instrument_code'] == 'EOS_EUR'][0]), 
        dXLM=float([d['price_change'] for d in data if d['instrument_code'] == 'XLM_EUR'][0]),
        )

    print('AWAKE AI!! AWAAAKE!! MUHA AHAHAHAHA 22022202')

    print(f'The observation is: {observation}')


    return observation

# def trade_ltc(con, prediction: float, spread:float, is_active:bool):

#     print(f'prediciton is of type: {type(prediction)}')
#     print(f'spread is of type: {type(spread)}')

#     # TODO: close open position if prediction is corrupt

#     if is_active and prediction < 0:
#         print('HERE IN THE IF')
#         con.close_all_for_symbol('LTC/USD')
#         is_active = False
#         print('LTC position closed')
#     elif not is_active and prediction > spread:
#         print('HERE IN THE ELIF')
#         con.create_market_buy_order('LTC/USD', 100)
#         is_active = True
#         print('LTC position opened')
#     else:
#         print(f'Do nothing. Spread: {spread}, prediction: {prediction}')

# def get_spread_ltc(con) -> float:
#     offers_df = con.get_offers(kind='dataframe')

#     print('DATAFRAME OFFERS')
#     print(offers_df.loc[offers_df['currency'] == 'LTC/USD'])

#     spread = offers_df.loc[offers_df['currency'] == 'LTC/USD']['spread'].values[0]

#     return float(spread)

def connect_and_trade(is_active:bool):
    try:
        print('CONNECT DO FUT PANDA')
        conn = http.client.HTTPSConnection("api.exchange.bitpanda.com")

        headers = { 'Accept': "application/json" }

        conn.request("GET", "/public/v1/market-ticker", headers=headers)

        prediction = float(predict_ltc(get_observation(conn)))

        print(f'The prediction is: {prediction}')

        # spread = get_spread_ltc(con)

        # print(f'The spread is: {spread}')


        # trade_ltc(con, prediction, spread, is_active)

        conn.close()

    except Exception as e:
        print(e)
        conn.close()



def gold_mule_shit():


    while True:
        connect_and_trade(False)
        time.sleep(20)


            

gold_mule_shit()

