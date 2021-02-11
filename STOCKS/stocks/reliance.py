import requests
import time
from pprint import pprint
from decouple import config
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BSE:RELIANCE&apikey=XYZ"
response = requests.get(url)
print(response.status_code)
# pprint(response.json())
df = pd.json_normalize(response.json())
pprint(df)