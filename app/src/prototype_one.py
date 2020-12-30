import os
import fxcmpy
import pandas
import time
from utils import time_convert
from predict import predict_cryptomajor_delta

PERIOD = 'm15'
ROWS = 2

start_time = time.time()

print('CONNECT TO FXCMPY API ...')
con = fxcmpy.fxcmpy(config_file=os.getenv('FXCM_CONFIG'), server='demo')
print(time_convert(time.time() - start_time))

print('FETCH INSTRUMENTS...')
assets = con.get_instruments_for_candles()
print(time_convert(time.time() - start_time))

# assets = ['BTC/USD','']

# XXX: Get historical data
last_interval = pandas.DataFrame()
for c in assets[:3]: #TODO no slicing for all assets
    try:
        print(f'Fetching {c}...')
        data = con.get_candles(c, period=PERIOD, number=ROWS)

        last_interval[c] = data['bidopen']
    except:
        print(f'Could not fetch {c}')

    print(time_convert(time.time() - start_time))

print(last_interval)

# XXX: Get account balance
account_info = con.get_accounts()
print('The account info')
print(account_info.T)

balance = account_info['balance'][0]
print(f'The balance is: {balance}')

equity = account_info['equity'][0]
print(f'The equity is: {balance}')

# XXX: Open order
order = con.create_market_sell_order('EUR/USD', 100)

print('created order')
print(order)

print('Open positions')
print(con.get_open_positions().T)

# XXX: Close order
order = con.close_all_for_symbol('EUR/USD')

print('closed order')
print(order)

print('Open positions')
print(con.get_open_positions().T)

con.close()
