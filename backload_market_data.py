import os
from data_access.database import post_market_data

path = 'C:/_data/MarketData/'

for files in os.listdir(path):
    os.chdir(path)
    print(os.path.abspath(files))
    post_market_data.from_yahoo_csv_adjusted_close(os.path.abspath(files))
