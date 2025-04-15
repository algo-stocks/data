import os
import zipfile
import requests
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


data = None
source='CafeF'


def set_source(src):
  """Set data source

  Keyword arguments:
  src ({'bnb', 'CafeF', 'CafeF.Raw', 'cophieu68'}) -- Data source
  """
  global source, data
  if src != source:
    source = src
    data = None


def load_data():
  """Load data from source
  """
  global data
  if not os.path.isfile('{}.feather.zip'.format(source)):
    r = requests.get('https://github.com/algo-stocks/data/releases/download/v2.0/{}.feather.zip'.format(source), allow_redirects=True)
    open('{}.feather.zip'.format(source), 'wb').write(r.content)
  
  data = pd.read_feather(zipfile.ZipFile('{}.feather.zip'.format(source)).open('{}.feather'.format(source)))
  return data


def get_pricing(symbol, start_date=None, end_date=None, frequency='daily', fields=None):
  """Get pricing

  Keyword arguments:
  symbol (str) -- Asset symbol
  start_date (str or pd.Timestamp, optional) -- String or Timestamp representing a start date or start intraday minute for the returned data. Defaults to None.
  end_date (str or pd.Timestamp, optional) -- String or Timestamp representing a start date or start intraday minute for the returned data. Defaults to None.
  frequency ({'daily'}, optional) -- Resolution of the data to be returned
  fields (str or list, optional) -- String or list drawn from {'open', 'high', 'low', 'close', 'volume'}. Default behavior is to return all fields.
  """
  usecols = None
  if fields is not None:
    if type(fields) is list:
      usecols = [field for field in fields]
    else:
      usecols = [fields]
  
  if data is None:
    load_data()
  
  symbol = symbol.upper()
  result = data[(data.ticker == symbol) | (data.ticker == f"^{symbol}")].set_index('date').sort_index()[start_date:end_date]
  result.ticker = symbol
  if fields is not None:
    if type(fields) is list:
      return result[[field for field in fields]]
    else:
      return result[[fields]]
  
  return result


def get_prices(*symbols, start_date=None, end_date=None, frequency='daily', field='close'):
  """Get prices

  Keyword arguments:
  symbols (list of str) -- Asset symbols
  start_date (str or pd.Timestamp, optional) -- String or Timestamp representing a start date or start intraday minute for the returned data. Defaults to None.
  end_date (str or pd.Timestamp, optional) -- String or Timestamp representing a start date or start intraday minute for the returned data. Defaults to None.
  frequency ({'daily'}, optional) -- Resolution of the data to be returned
  field (str, optional) -- String or list drawn from {'open', 'high', 'low', 'close', 'volume'}. Default behavior is to return 'close'.
  """
  prices = None
  for symbol in symbols:
    price = get_pricing(symbol, start_date=start_date, end_date=end_date, frequency=frequency, fields=field)
    if price is None:
      continue
    
    price = price.rename(columns={field: symbol})
    if prices is None:
      prices = price
    else:
      prices = prices.join(price)
  
  return prices
