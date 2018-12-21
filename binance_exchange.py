from binance.client import Client
from user import getbinanceapi
import time
import sys


def getbinanceticker(chat_id, ticker):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()

	client = Client(api_key, api_secret)
	binance_timesync(client)
	ticker = client.get_symbol_ticker(symbol=ticker)
	print(ticker)

	return ticker


def binance_get_recent_trades(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)

	binance_timesync(client)

	try:
		js_info = client.get_recent_trades(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_getbalances(chat_id):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)

	binance_timesync(client)

	try:
		js_info = client.get_account()
		return js_info
	except Exception as e:
		print(e)


def binance_getbalance(chat_id, asset):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)

	try:
		js_info = client.get_asset_balance(asset = asset)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def getbinancehistory(chat_id):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)


def binance_open_orders(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.get_open_orders(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_cancel_order(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.cancel_order(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)

def binance_get_my_trades(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.cancel_order(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_get_all_tickers(chat_id):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	js_info = []
	try:
		js_info = client.get_all_tickers()
		#print(js_info)
		return js_info
	except Exception as e:
		print(e)
	return js_info



def binancecancel_order(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	js_info = []
	try:
		js_info = client.cancel_order(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)
	return js_info


def binance_get_open_orders(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.get_open_orders(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_get_all_orders(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.get_all_orders(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_get_order(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.get_order(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_get_symbol_ticker(chat_id, symbol):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.get_symbol_ticker()
		for t in js_info:
			if t['symbol'] == symbol:
				return t['price']
	except Exception as e:
		print (e)
	return None


def binance_get_server_time(chat_id):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	server_time = client.get_server_time()
	return server_time


def binance_timesync(client):
	gt = client.get_server_time()
	gg = int(gt['serverTime'])
	ff = gg - 10799260
	uu = ff / 1000
	yy = int(uu)
	tt = time.localtime(yy)

	if sys.platform == 'linux2':
		pass

	elif  sys.platform == 'win32':
		import win32api
		#print(tt)
		win32api.SetSystemTime(tt[0], tt[1], 0, tt[2], tt[3], tt[4], tt[5], 0)


def binance_create_test_order(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)

	try:
		binance_timesync(client)

		js_info = client.create_test_order(**params)
		print(js_info)
	except Exception as e:
		print (e)
	return None

def binance_order_market_buy(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.order_market_buy(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_order_market_sell(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.order_market_sell(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_order_limit_sell(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.order_limit_sell(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_order_limit_buy(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.order_limit_buy(**params)
		return js_info
	except Exception as e:
		return str(e)


def binance_create_order(chat_id, **params):
	full_api = getbinanceapi(chat_id)['binance_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Client(api_key, api_secret)
	binance_timesync(client)
	try:
		js_info = client.create_order(**params)
		return js_info
	except Exception as e:
		print(e)
		return str(e)

