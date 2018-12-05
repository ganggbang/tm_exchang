from binance.client import Client
#from user import getbinanceapi
import time
import win32api

def getbinanceticker(api_key, api_secret, ticker):
	client = Client(api_key, api_secret)
	ticker = client.get_symbol_ticker(symbol=ticker)
	print(ticker)

	return ticker


def binance_getbalances(api_key, api_secret):
	client = Client(api_key, api_secret)

	binance_timesync(client)

	try:
		js_info = client.get_account()
		return js_info
	except Exception as e:
		print(e)


def binance_getbalance(api_key, api_secret):
	client = Client(api_key, api_secret)

	binance_timesync(client)
	#js_info = client.get_account(timestamp=time.time())

	try:
		js_info = client.get_asset_balance(asset = 'BTC')
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def getbinancehistory(api_key, api_secret):
	client = Client(api_key, api_secret)


def binance_open_orders(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.get_open_orders(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_cancel_order(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.cancel_order(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binancecancel_order(api_key, api_secret, **params):
	client = Client(api_key, api_secret)
	try:
		js_info = client.cancel_order(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_get_open_orders(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.get_open_orders(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_get_all_orders(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.get_all_orders(**params)
		print(js_info)
		return js_info
	except Exception as e:
		print(e)


def binance_get_order(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.get_order(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_get_symbol_ticker(api_key, api_secret, symbol):
	client = Client(api_key, api_secret)

	try:
		js_info = client.get_symbol_ticker()
		for t in js_info:
			if t['symbol'] == symbol:
				return t['price']
	except Exception as e:
		print (e)
	return None

def binance_timesync(client):
	gt = client.get_server_time()
	#print(gt['serverTime'])
	#print(time.localtime())
	gg = int(gt['serverTime'])
	ff = gg - 10799260
	uu = ff / 1000
	yy = int(uu)
	tt = time.localtime(yy)
	#print(tt)
	win32api.SetSystemTime(tt[0], tt[1], 0, tt[2], tt[3], tt[4], tt[5], 0)


def binance_create_test_order(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		binance_timesync(api_key, api_secret)

		js_info = client.create_test_order(**params)
		print(js_info)
	except Exception as e:
		print (e)
	return None

def binance_order_market_buy(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.order_market_buy(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_order_market_sell(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.order_market_sell(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_order_limit_sell(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.order_limit_sell(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_order_limit_buy(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.order_limit_buy(**params)
		return js_info
	except Exception as e:
		print(e)


def binance_create_order(api_key, api_secret, **params):
	client = Client(api_key, api_secret)

	try:
		js_info = client.create_order(**params)
		return js_info
	except Exception as e:
		print(e)
	return None

