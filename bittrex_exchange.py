from bittrex.bittrex import Bittrex, API_V2_0, API_V1_1
from user import getbittrexapi

def bittrex_getbalances(chat_id):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)
	try:
		r = client.get_balances()
		print(r)
		return r
	except Exception as e:
		print(e)


def bittrex_getbalance(chat_id, cur):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)
	try:
		r = client.get_balance(cur)
		print(r)
		return r
	except Exception as e:
		print(e)


def bittrex_get_orderbook(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		r = client.get_orderbook(**params)
		print(r)
		return r
	except Exception as e:
		print(e)


def bittrex_getticker(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)
	try:
		r = client.get_ticker(**params)
		print(r)
		return r
	except Exception as e:
		print(e)


def bittrex_buy_limit(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.buy_limit(**params)
		print(result)
		return result
	except Exception as e:
		print(e)


def bittrex_sell_limit(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.sell_limit(**params)
		print(result)
		return result
	except Exception as e:
		print(e)

def bittrex_get_order_history(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.get_order_history(**params)
		print(result)
		return result
	except Exception as e:
		print(e)

def bittrex_get_open_orders(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.get_open_orders(**params)
		print(result)
		return result
	except Exception as e:
		print(e)


def bittrex_cancel(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.cancel(**params)
		print(result)
		return result
	except Exception as e:
		print(e)


def bittrex_get_order(chat_id, **params):
	full_api = getbittrexapi(chat_id)['bittrex_api']
	api_key = full_api.split(':')[0].strip()
	api_secret = full_api.split(':')[1].strip()
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.get_order(**params)
		print(result)
		return result
	except Exception as e:
		print(e)

