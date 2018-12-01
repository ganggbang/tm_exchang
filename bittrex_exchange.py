from bittrex.bittrex import Bittrex, API_V2_0, API_V1_1

def getbittrexbalance(api_key, api_secret):
	my_bittrex = Bittrex(api_key, api_secret, api_version=API_V1_1)  
	r = my_bittrex.get_balance('BTC')
	print(r)
	return r

def getbittrexticker(api_key, api_secret, ticker):
	my_bittrex = Bittrex(api_key, api_secret, api_version=API_V1_1)  
	r = my_bittrex.get_ticker(ticker)
	return r
