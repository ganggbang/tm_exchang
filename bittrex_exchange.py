from bittrex.bittrex import Bittrex, API_V2_0, API_V1_1


def bittrex_getbalances(api_key, api_secret):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)
	try:
		r = client.get_balances()
		print(r)
		return r
	except Exception as e:
		print(e)


def bittrex_getbalance(api_key, api_secret, cur):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)
	try:
		r = client.get_balance(cur)
		print(r)
		return r
	except Exception as e:
		print(e)


def bittrex_getticker(api_key, api_secret, **params):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)
	try:
		r = client.get_ticker(**params)
		print(r)
		return r
	except Exception as e:
		print(e)


def bittrex_buy_limit(api_key, api_secret, **params):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.buy_limit(**params)
		print(result)
		return result
	except Exception as e:
		print(e)


def bittrex_sell_limit(api_key, api_secret, **params):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.sell_limit(**params)
		print(result)
		return result
	except Exception as e:
		print(e)

def bittrex_get_order_history(api_key, api_secret, **params):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.get_order_history(**params)
		print(result)
		return result
	except Exception as e:
		print(e)

def bittrex_get_open_orders(api_key, api_secret, **params):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.get_open_orders(**params)
		print(result)
		return result
	except Exception as e:
		print(e)


def bittrex_cancel(api_key, api_secret, **params):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.cancel(**params)
		print(result)
		return result
	except Exception as e:
		print(e)


def bittrex_get_order(api_key, api_secret, **params):
	client = Bittrex(api_key, api_secret, api_version=API_V1_1)

	try:
		result = client.get_order(**params)
		print(result)
		return result
	except Exception as e:
		print(e)

