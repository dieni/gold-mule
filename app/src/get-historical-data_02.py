'''
Get the historical data by defining the period and the number of rows. Max. 10'000 rows.
'''
import os
import fxcmpy
import pandas
import time
import datetime as dt
from utils import time_convert

PERIOD = 'm1'
DAYS = 2
DAYS_MULTIPLICATOR = 1 # limited to 10 000 rows per request. 1440 rows when m1 per day
THRESH = 0.95
OUTPUT = f"{os.getenv('DATA_PATH')}currencies_{DAYS}_{DAYS_MULTIPLICATOR}_{str(PERIOD)}_{str(THRESH)}.csv"

start_time = time.time()

print('CONNECT TO FXCMPY API ...')
con = fxcmpy.fxcmpy(config_file=os.getenv('FXCM_CONFIG'), server='demo')
print(time_convert(time.time() - start_time))

print('FETCH INSTRUMENTS...')
currencies = con.get_instruments_for_candles()
print(time_convert(time.time() - start_time))


progress = 0
currencyT = pandas.DataFrame()
now = dt.datetime.utcnow()
for day in range(DAYS):
    now = now - dt.timedelta(hours=24*DAYS_MULTIPLICATOR)
    currency_per_iterationT = pandas.DataFrame()
    for c in currencies:
        progress = round((day*len(currencies))/(DAYS*len(currencies)), 2)
        print(f'The the current progress is {str(progress)}%. Time to fetch {now}')
        try:

            print(f'Fetching {c}...')
            data = con.get_candles(c, period=PERIOD, start=now, stop=now + dt.timedelta(hours=24*DAYS_MULTIPLICATOR))

            if data.size > 0:
                print(f'Incoming Data Shape: {data.shape}')
                currency_per_iterationT[c] = data['bidopen']
                print(f'Temp Shape: {currency_per_iterationT.shape}')
        except:
            print(f'Could not fetch {c}')

        print(time_convert(time.time() - start_time))

    currencyT = currencyT.append(currency_per_iterationT)

# REMOVE ALL COLUMNS THAT CONTAIN A NAN GREATER THAN A CERTAIN THRESHOLD
#currencyT = currencyT.dropna(axis=1, thresh=currencyT.shape[0]*THRESH)

#currencyT = currencyT.dropna(axis=0, how='any')


print(currencyT)
print(f'The lenght of the table is {currencyT.shape[0]}')
print(f'Number of currencies: {len(currencyT.columns)}')
print(f'Number of data elements: {currencyT.size}')


currencyT.to_csv(OUTPUT)
con.close()
