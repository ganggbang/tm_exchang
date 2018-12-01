from binance.client import Client
from user import getbinanceapi 
import time


def getbinanceticker(api_key, api_secret, ticker):
	client = Client(api_key, api_secret)
	ticker = client.get_symbol_ticker(symbol=ticker)
	print(ticker)

	return ticker


def getbinancebalance(api_key, api_secret):
	client = Client(api_key, api_secret)

	#js_info = client.get_account(timestamp=time.time())
	js_info = client.get_asset_balance(asset = 'BTC')
	print(js_info)

	return js_info

def getbinancehistory(api_key, api_secret):
	client = Client(api_key, api_secret)