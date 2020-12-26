'''
Get the historical data by defining the period and the number of days. Unlimited rows.
'''
import os
import fxcmpy
import pandas
import time
from utils import time_convert

PERIOD = 'm15'
ROWS = 100 # max 10'000
THRESH = 0.95
OUTPUT = f"{os.getenv('DATA_PATH')}currencies_{ROWS}_{str(PERIOD)}_{str(THRESH)}.csv"

start_time = time.time()

print('CONNECT TO FXCMPY API ...')
con = fxcmpy.fxcmpy(config_file=os.getenv('FXCM_CONFIG'), server='demo')
print(time_convert(time.time() - start_time))

print('FETCH INSTRUMENTS...')
instruments = con.get_instruments_for_candles()
print(time_convert(time.time() - start_time))

CURRENCIES = instruments
print(instruments)

currencyT = pandas.DataFrame()
for c in CURRENCIES:
    try:
        print(f'Fetching {c}...')
        data = con.get_candles(c, period=PERIOD, number=ROWS)

        currencyT[c] = data['bidopen']
    except:
        print(f'Could not fetch {c}')

    print(time_convert(time.time() - start_time))

# REMOVE ALL COLUMNS THAT CONTAIN A NAN
currencyT = currencyT.dropna(axis=1, thresh=ROWS*THRESH)

print(currencyT)
print(f'Number of currencies: {len(currencyT.columns)}')
print(f'Number of data elements: {currencyT.size}')


currencyT.to_csv(OUTPUT)
con.close()
