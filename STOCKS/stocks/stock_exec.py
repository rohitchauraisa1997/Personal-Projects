import requests
from pprint import pprint
import time
from decouple import config
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BSE:PIIND&apikey=XYZ"
response = requests.get(url)
print(response.status_code)
pprint(response.json())
# api_key = (config("api_key"))
# # api_key = "XYZ"
# ts = TimeSeries(key=api_key, output_format="pandas")
# data, metadata = ts.get_intraday(symbol="NSE:PIIND", interval="60min", outputsize="full")
# print(data)
# print("*"*100)
# print(metadata)