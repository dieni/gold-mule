import os
import fxcmpy
import pandas
import time
from utils import time_convert
from predict import predict_cryptomajor_delta
from models import Observation

PERIOD = 'm1'
ROWS = 2

start_time = time.time()

print('CONNECT TO FXCMPY API ...')
con = fxcmpy.fxcmpy(config_file=os.getenv('FXCM_CONFIG'), server='demo')
print(time_convert(time.time() - start_time))

# print('FETCH INSTRUMENTS...')
# assets = con.get_instruments_for_candles()
# print(time_convert(time.time() - start_time))

assets = ['BTC/USD', 'BCH/USD', 'ETH/USD', 'LTC/USD', 'XRP/USD', 'EOS/USD', 'XLM/USD', 'CryptoMajor']

# XXX: Get historical data
last_interval = pandas.DataFrame()
for c in assets:
    try:
        print(f'Fetching {c}...')
        data = con.get_candles(c, period=PERIOD, number=ROWS)

        last_interval[c] = data['bidopen']
    except:
        print(f'Could not fetch {c}')

    print(time_convert(time.time() - start_time))

print(last_interval)

observation1 = Observation(BTC=last_interval['BTC/USD'][0], BCH=last_interval['BCH/USD'][0], ETH=last_interval['ETH/USD'][0], LTC=last_interval['LTC/USD'][0], XRP=last_interval['XRP/USD'][0], EOS=last_interval['EOS/USD'][0], XLM=last_interval['XLM/USD'][0], CryptoMajor=1, CryptoMajor_delta=1)
observation2 = Observation(BTC=last_interval['BTC/USD'][1], BCH=last_interval['BCH/USD'][1], ETH=last_interval['ETH/USD'][1], LTC=last_interval['LTC/USD'][1], XRP=last_interval['XRP/USD'][1], EOS=last_interval['EOS/USD'][1], XLM=last_interval['XLM/USD'][1], CryptoMajor=1, CryptoMajor_delta=1)


print(observation1)
print(observation2)

print(predict_cryptomajor_delta())

# XXX: Get account balance
account_info = con.get_accounts()
print('The account info')
print(account_info.T)

balance = account_info['balance'][0]
print(f'The balance is: {balance}')

equity = account_info['equity'][0]
print(f'The equity is: {balance}')

# # XXX: Open order
# order = con.create_market_sell_order('EUR/USD', 100)

# print('created order')
# print(order)

# print('Open positions')
# print(con.get_open_positions().T)

# # XXX: Close order
# order = con.close_all_for_symbol('EUR/USD')

# print('closed order')
# print(order)

# print('Open positions')
# print(con.get_open_positions().T)

con.close()
