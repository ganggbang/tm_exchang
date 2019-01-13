#!/usr/bin/python3

from user import *
from binance_exchange import *
from bittrex_exchange import *
import telegram
import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################

bot = telegram.Bot(token='692136526:AAGbRDOH2uO35F6Em843eQDVLpiW6MFcLmk')


def broadcastmessage_keyboard(message_id):
	keyboard = [[InlineKeyboardButton('Yes', callback_data='bmy_'+str(message_id))],
			[InlineKeyboardButton('No', callback_data='bmn_'+str(message_id))],]
	return InlineKeyboardMarkup(keyboard)


def sendbroadcastmessages(bot, chat_id, message, message_id):
	try:
		m = re.search(r"(.*):(.*)@(.*)", message)
		if m.group(0) and m.group(1) and m.group(2) and m.group(3):
			symbol = str(m.group(1)).upper()
			exchange = str(m.group(2)).upper()
			price = str(m.group(3)).upper()

			if exchange == 'BINANCE':
				ticker_price = binance_get_symbol_ticker(chat_id, symbol)
				#insert_order(chat_id, symbol, 'BINANCE')
			elif exchange == 'BITTREX':
				ticker_price = bittrex_getticker(chat_id, market=symbol)['result']['Ask']
				#insert_order(chat_id, symbol, 'BITTREX')

			msg = "New buy idea for '" + symbol + "' (ticker), trade on '" + exchange + "' (exchange) for "+str(price)+". Current price at '" + str(ticker_price) + "' (satoshi price) BTC"
			bot.send_message(chat_id=chat_id, text=msg, reply_markup=broadcastmessage_keyboard(message_id))
	except Exception as e:
		print(e)

messages = getbroadcastmessages()
users = get_users()
for user in users:
	take_profit = get_take_profit(user['tm_id'])
	orders = get_orders_by_filled(0, user['tm_id'])

	for order in orders:
		if order['exchange'].upper() == 'BITTREX':
			bit_order = bittrex_get_order(user['tm_id'], uuid = order['orderId'])
			current_price = bittrex_getticker(user['tm_id'], market = order['ticker'])['result']['Ask']
			p = get_howpercentage(current_price, bit_order['result']['Price'])
			if p >= 100 + take_profit:
				bittrex_sell_limit(user['tm_id'], quantity = order['quantity'], market = order['ticker'], rate = current_price)
		elif order['exchange'].upper() == 'BINANCE':
			bin_order = binance_get_order(user['tm_id'], symbol = order['ticker'], orderId = order['orderId'])
			current_price = binance_get_symbol_ticker(user['tm_id'], symbol=order['ticker'])
			p = get_howpercentage(current_price, bin_order['price'])
			if p >= 100 + take_profit:
				r = binance_order_limit_sell(user['tm_id'], symbol = order['ticker'], quantity = order['quantity'], price = current_price)

	for msg in messages:
		try:
			for uc in get_usingchannels_byuserid(user['tm_id']):
				if msg['channel_id'] == uc['channel_id']:
					sendbroadcastmessages(bot, user['tm_id'], msg['message'], msg['id'])
		except Exception as e:
			print(e)
