import os
import fxcmpy
import pandas
import time
from predict import predict_ltc
from models import Observation
from datetime import datetime

PERIOD = 'm1'
ROWS = 2
ASSETS = ['BTC/USD', 'BCH/USD', 'ETH/USD', 'LTC/USD', 'XRP/USD', 'EOS/USD', 'XLM/USD']
# is_active = False

def get_observation(con):

    # XXX: Get historical data
    last_interval = pandas.DataFrame()
    for c in ASSETS:
        try:
            print(f'Fetching {c}...')
            data = con.get_candles(c, period=PERIOD, number=ROWS)

            last_interval[c] = data['bidopen']
        except:
            print(f'Could not fetch {c}')


    print(last_interval)

    observation = Observation(
        BTC=last_interval['BTC/USD'][1], 
        BCH=last_interval['BCH/USD'][1], 
        ETH=last_interval['ETH/USD'][1], 
        LTC=last_interval['LTC/USD'][1], 
        XRP=last_interval['XRP/USD'][1], 
        EOS=last_interval['EOS/USD'][1], 
        XLM=last_interval['XLM/USD'][1],
        dBTC=last_interval['BTC/USD'][1] - last_interval['BTC/USD'][0], 
        dBCH=last_interval['BCH/USD'][1] - last_interval['BCH/USD'][0], 
        dETH=last_interval['ETH/USD'][1] - last_interval['ETH/USD'][0], 
        dLTC=last_interval['LTC/USD'][1] - last_interval['LTC/USD'][0], 
        dXRP=last_interval['XRP/USD'][1] - last_interval['XRP/USD'][0], 
        dEOS=last_interval['EOS/USD'][1] - last_interval['EOS/USD'][0], 
        dXLM=last_interval['XLM/USD'][1] - last_interval['XLM/USD'][0],
        )

    print(f'The observation is: {observation}')

    return observation

def trade_ltc(con, prediction: float, spread:float, is_active:bool):

    print(f'prediciton is of type: {type(prediction)}')
    print(f'spread is of type: {type(spread)}')

    # TODO: close open position if prediction is corrupt

    if is_active and prediction < 0:
        print('HERE IN THE IF')
        con.close_all_for_symbol('LTC/USD')
        is_active = False
        print('LTC position closed')
    elif not is_active and prediction > spread:
        print('HERE IN THE ELIF')
        con.create_market_buy_order('LTC/USD', 100)
        is_active = True
        print('LTC position opened')
    else:
        print(f'Do nothing. Spread: {spread}, prediction: {prediction}')

def get_spread_ltc(con) -> float:
    offers_df = con.get_offers(kind='dataframe')

    print('DATAFRAME OFFERS')
    print(offers_df.loc[offers_df['currency'] == 'LTC/USD'])

    spread = offers_df.loc[offers_df['currency'] == 'LTC/USD']['spread'].values[0]

    return float(spread)

def connect_and_trade(is_active:bool):
    try:
        print('CONNECT TO FXCMPY API ...')
        con = fxcmpy.fxcmpy(config_file=os.getenv('FXCM_CONFIG'), server='demo')
        

        prediction = float(predict_ltc(get_observation(con)))
        prediction = -1.0 # TODO: REMOVE! only for test purposes

        print(f'The prediction is: {prediction}')

        spread = get_spread_ltc(con)

        print(f'The spread is: {spread}')


        trade_ltc(con, prediction, spread, is_active)

        con.close()

    except Exception as e:
        print(e)
        con.close()



def gold_mule_shit():
    is_active= False
    while True:
        current_second = datetime.now().second

        if (current_second % 20) == 0:
            try:    
                connect_and_trade(is_active)
            except:
                pass

        time.sleep(0.1)
            

gold_mule_shit()

