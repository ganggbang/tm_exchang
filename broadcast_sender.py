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

			full_api = getbinanceapi(chat_id)['binance_api']

			# print(full_api)
			api_key = full_api.split(':')[0].strip()
			api_secret = full_api.split(':')[1].strip()
			ticket_price = binance_get_symbol_ticker(api_key, api_secret, symbol+'BTC')

			#print(symbol_ticket)

			msg = "New buy idea for '" + symbol + "' (ticker), trade on '" + exchange + "' (exchange). Current price at '" + ticket_price + "' (satoshi price) BTC"
			bot.send_message(chat_id=chat_id, text=msg, reply_markup=broadcastmessage_keyboard(message_id))
	except Exception as e:
		print(e)


messages = getbroadcastmessages()

for msg in messages:
	try:
		print(msg)
		sendbroadcastmessages(bot, msg['tm_id'], msg['message'], msg['id'])
	except Exception as e:
		print(e)
	#setbroadcastmessages_sended(msg['id'])
