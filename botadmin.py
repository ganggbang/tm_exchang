#!/usr/bin/python3
import pymysql
import logging
import re
from admin import *
from binance_exchange import *
from bittrex_exchange import * 
from connection import create_connection
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler,
						  ConversationHandler)
############################### Bot ############################################

def start(bot, update):
	update.message.reply_text(main_menu_message(),
		reply_markup=main_menu_keyboard())

def reg_menu(bot, update):
	query = update.callback_query
	#reply_markup = InlineKeyboardMarkup(keyboard)
	bot.send_message(chat_id=query.message.chat_id,
		text='Give your channel a name')
	return REGISTER

def main_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			text=main_menu_message(),
			reply_markup=main_menu_keyboard())

def view_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			text=view_menu_message(),
			reply_markup=view_menu_keyboard())

def view_submenu1(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=view_submenu1_message(),
		reply_markup=view_submenu1_keyboard())

def select_channels_adminmenu(bot, update):
	query = update.callback_query

	channels = get_binancechannels_admin()
	keyboard = []

	for ch in channels:
		if ch['is_enable'] == 1:
			keyboard.append([InlineKeyboardButton(ch['channel_name'], callback_data='vs1_21'+str(ch['id']))])
		else:
			keyboard.append([InlineKeyboardButton('* '+ch['channel_name'], callback_data='vs1_21'+str(ch['id']))])
	keyboard.append([InlineKeyboardButton('View menu', callback_data='view')])

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=select_channels_message(),
		reply_markup=InlineKeyboardMarkup(keyboard))

def view_editdefaultmessage(bot, update):
	query = update.callback_query
	bot.send_message(chat_id=query.message.chat_id,
		text="To change your default message, you'll be needed to specify these variables for the followng: type 'x' to specify ticker, type 'z' to specify exchange, and type 'y' to specify price")

	return VIEW_DEFAULTMESSAGE

def view_submenu2(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=view_submenu2_message(),
		reply_markup=view_submenu2_keyboard())

def view_submenu3(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=view_submenu3_message(),
		reply_markup=view_submenu3_keyboard())

def post_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=post_menu_message(),
		reply_markup=post_menu_keyboard())

# def post_submenu1(bot, update):
# 	query = update.callback_query
# 	text = update.message.text
# 	bot.send_message(chat_id=query.message.chat_id,
# 		text='Exchange Binance selected, type ticker name paired with BTC, so for BTC-LSK type \'LSK\'')
# 	# bot.edit_message_text(chat_id=query.message.chat_id,
# 	# 	message_id=query.message.message_id,
# 	# 	text=post_submenu1_message(),
# 	# 	reply_markup=post_submenu1_keyboard())
# 	return POST1
#
# def post_submenu2(bot, update):
# 	query = update.callback_query
# 	text = update.message.text
# 	bot.send_message(chat_id=query.message.chat_id,
# 		text='Exchange Bittrex selected, type ticker name paired with BTC, so for BTC-LSK type \'LSK\'')
# 	# bot.edit_message_text(chat_id=query.message.chat_id,
# 	# 	message_id=query.message.message_id,
# 	# 	text=post_submenu2_message(),
# 	# 	reply_markup=post_submenu2_keyboard())
# 	return POST2



############################ Keyboards #########################################


def main_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Register', callback_data='register')],
							[InlineKeyboardButton('Post Trade', callback_data='post')],
							[InlineKeyboardButton('View', callback_data='view')]]
	return InlineKeyboardMarkup(keyboard)


def view_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Registered Members', callback_data='vs1')],
							[InlineKeyboardButton('ChannelID', callback_data='vs2')],
							[InlineKeyboardButton('Broadcast Message', callback_data='vs3')],
							[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)

def view_submenu1_keyboard():
	keyboard = [[InlineKeyboardButton('Total Members', callback_data='vs1_11')],
							[InlineKeyboardButton('Active Members', callback_data='vs1_12')],
							[InlineKeyboardButton('Inactive or Disabled Members', callback_data='vs1_12')],
							[InlineKeyboardButton('View menu', callback_data='view')]]
	return InlineKeyboardMarkup(keyboard)

def view_submenu2_keyboard():
	keyboard = [[InlineKeyboardButton('Edit Channel Name', callback_data='vs1_21')],
							[InlineKeyboardButton('View ChannelID', callback_data='vs1_22')],
							[InlineKeyboardButton('View menu', callback_data='view')]]
	return InlineKeyboardMarkup(keyboard)

def view_submenu3_keyboard():
	keyboard = [[InlineKeyboardButton('Edit Default Message', callback_data='vs1_31')],
							[InlineKeyboardButton('Restore default message', callback_data='vs1_32')],
							[InlineKeyboardButton('View menu', callback_data='view')]]
	return InlineKeyboardMarkup(keyboard)

def post_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Binance', callback_data='ps1')],
							[InlineKeyboardButton('Bittrex', callback_data='ps2')],
							[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)

def post_submenu_keyboard(channel_id):
	keyboard = [[InlineKeyboardButton('Default Message', callback_data='default_'+str(channel_id))],
							[InlineKeyboardButton('Custom Message', callback_data='custom_'+str(channel_id))],
							[InlineKeyboardButton('Post menu', callback_data='post')]]
	return InlineKeyboardMarkup(keyboard)

# def post_submenu2_keyboard():
# 	keyboard = [[InlineKeyboardButton('Default Message', callback_data='ps2_1')],
# 							[InlineKeyboardButton('Custom Message', callback_data='ps2_2')],
# 							[InlineKeyboardButton('Post menu', callback_data='post')]]
# 	return InlineKeyboardMarkup(keyboard)

def view_broadcast_yn_keyboard(channel_id):
	keyboard = [[InlineKeyboardButton('Yes', callback_data='vs_by_'+str(channel_id))],
							[InlineKeyboardButton('No', callback_data='vs_bn')],
							[InlineKeyboardButton('View menu', callback_data='view')]]
	return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def reg_menu_message():
	return 'Give your channel a name'

def main_menu_message():
	return 'Choose the option in menu:'

def view_menu_message():
	return 'Choose the option in menu:'

def view_submenu1_message():
	return 'Choose the option in menu:'

def view_submenu2_message():
	return 'Choose the option in menu:'

def view_submenu3_message():
	return 'Choose the option in menu:'

def post_menu_message():
	return 'Choose the option in menu:'

def post_submenu_message():
	return 'Choose the option in menu:'

# def post_submenu2_message():
# 	return 'Choose the option in menu:'

def select_channels_message():
	return 'Choose the channel in menu:'

def channel_choice(bot, update, user_data):
	text = update.message.text
	createChannel(text)

	update.message.reply_text('Your {} ChannelID created, go to View > ChannelID to copy'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END

def edit_defaultmessage(bot, update, user_data):
	text = update.message.text

	update.message.reply_text('New default messaged saved.',
		reply_markup=view_menu_keyboard())

	return ConversationHandler.END

def view_editchannelname(bot, update, user_data):
	query = update.callback_query
	
	user_data['channel_id'] = query['data'].replace('vs1_21', '')

	bot.send_message(chat_id=query.message.chat_id,
		text='Type channel name limited to 20 characters')
	return VIEW

def edit_channelname(bot, update, user_data):
	text = update.message.text

	channel_id = user_data['channel_id']
	channel_name = text
	del user_data['channel_id']

	change_channelname(channel_id, channel_name)

	update.message.reply_text('Do you wish to broadcast message to users informing them of your name change?',
		reply_markup=view_broadcast_yn_keyboard(channel_id))


def send_broadcastmessage(bot, update):
	query = update.callback_query
	q = query['data'].replace('vs_b', '')

	ch = getchannelbyid(q[2:])
	if(q[0:1] == 'y'):
		users = getusers_forbroadcastmessage()
		for u in users:
			addbroadcastmsg(u['tm_id'], 'Announcement: Channel "'+ch['oldchannel_name']+'" has changed their name to "'+ch['channel_name']+'"')

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=main_menu_message(),
		reply_markup=main_menu_keyboard())	


def ticker_binance_choiced(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	channel_id = query['data'].replace('channel_binance_', '')

	bot.edit_message_text(chat_id=chat_id,
						  message_id=query.message.message_id,
						  text="Choose the option in menu :",
						  reply_markup=post_submenu_keyboard(channel_id))


def ticker_binance_choice(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	channels = get_binancechannels_admin()
	keyboard = []

	try:
		i = 0
		buttons = []
		keyboard.append([InlineKeyboardButton("Post Trade", callback_data='post')])
		for channel in channels:
			if "BTC" in channel['channel_name']:
				#print(channel['channel_name'])
				i = i + 1
				buttons.append(InlineKeyboardButton(channel['channel_name'], callback_data='channel_binance_'+str(channel['id'])))
				if i == 5:
					i = 0
					keyboard.append(buttons)
					buttons = []

		keyboard.append([InlineKeyboardButton("Post Trade", callback_data='post')])

		bot.edit_message_text(chat_id=chat_id,
						  message_id=query.message.message_id,
						  text="Choose the option in menu                              :",
						  reply_markup=InlineKeyboardMarkup(keyboard))
	except Exception as e:
		print(e)
	# assets = binance_get_all_tickers(user_id)
	# for asset in assets:
	# 	save('channels', data ={
	# 		'ticker':asset['symbol'],
	# 		'channel_name':asset['symbol'],
	# 		'is_bittrex':'0',
	# 		'is_enable':'1',
	# 	})


def ticker_bittrex_choiced(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	channel_id = query['data'].replace('channel_bittrex_', '')

	bot.edit_message_text(chat_id=chat_id,
						  message_id=query.message.message_id,
						  text="Choose the option in menu :",
						  reply_markup=post_submenu_keyboard(channel_id))

def ticker_bittrex_choice(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	channels = get_bittrexchannels_admin()
	keyboard = []

	try:
		i = 0
		buttons = []
		keyboard.append([InlineKeyboardButton("Post Trade", callback_data='post')])
		for channel in channels:
			if "BTC" in channel['channel_name']:
				#print(channel['channel_name'])
				i = i + 1
				buttons.append(InlineKeyboardButton(channel['channel_name'], callback_data='channel_bittrex_'+str(channel['id'])))
				if i == 5:
					i = 0
					keyboard.append(buttons)
					buttons = []

		keyboard.append([InlineKeyboardButton("Post Trade", callback_data='post')])

		bot.edit_message_text(chat_id=chat_id,
						  message_id=query.message.message_id,
						  text="Choose the option in menu                              :",
						  reply_markup=InlineKeyboardMarkup(keyboard))
	except Exception as e:
		print(e)
	# ticker = bittrex_getticker(user_id, text)
	# if ticker:
	# 	update.message.reply_text('Your {} ticker is valid'.format(text),
	# 		reply_markup=post_submenu2_keyboard())
	# else:
	# 	update.message.reply_text('Your {} ticker is not valid'.format(text),
	# 		reply_markup=post_submenu2_keyboard())


def custom_choice(bot, update):
	update.message.reply_text('')

	return MAIN_MENU

def post_submenu1(bot, update):
	text = update.message.text

	update.message.reply_text(
		"Broadcast has been sent to users for 'x' on 'z':",
		reply_markup=main_menu_keyboard()
	)

	return ConversationHandler.END


# def received_information(bot, update, user_data):
# 	text = update.message.text
# 	category = user_data['choice']
# 	user_data[category] = text
# 	del user_data['choice']

# 	update.message.reply_text("Neat! Just so you know, this is what you already told me:"
# 							  "{}"
# 							  "You can tell me more, or change your opinion on something.".format(
# 								  facts_to_str(user_data)), reply_markup=markup)

# 	return CHOOSING

def default_msg(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	channel_id = query['data'].replace('default_', '')

	bot.edit_message_text(chat_id=chat_id,
		message_id=query.message.message_id,
		text="Broadcast has been sent to users for 'x' on 'z':",
		reply_markup=main_menu_keyboard(),)

	return ConversationHandler.END


def custom_msg(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	channel_id = query['data'].replace('custom_', '')
	bot.edit_message_text(chat_id=chat_id,
		message_id=query.message.message_id,
		text="type 'x' to specify ticker, type 'z' to specify exchange, and type 'y' to specify price:",
		)

	return POST


def done(bot, update, user_data):

	return ConversationHandler.END


def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

REGISTER, MAIN_MENU, POST, VIEW, VIEW_DEFAULTMESSAGE = range(5)

# reply_keyboard = [['1', '2'],
# 				  ['3', '4'],
# 				  ['Done']]
#
# markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

############################# Handlers #########################################
updater = Updater('637840473:AAHi-_WkFXq8kTXSQyUR7dw5arDxW0Zaje4')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))

#updater.dispatcher.add_handler(CallbackQueryHandler(reg_menu, pattern='register'))
updater.dispatcher.add_handler(CallbackQueryHandler(post_menu, pattern='post'))
#updater.dispatcher.add_handler(CallbackQueryHandler(post_submenu1, pattern='ps1'))
updater.dispatcher.add_handler(CallbackQueryHandler(send_broadcastmessage, pattern='^vs_b'))

updater.dispatcher.add_handler(CallbackQueryHandler(view_menu, pattern='view'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu1, pattern='^vs1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu2, pattern='^vs2$'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu3, pattern='^vs3$'))

updater.dispatcher.add_handler(CallbackQueryHandler(select_channels_adminmenu, pattern='^vs1_21$'))
updater.dispatcher.add_handler(CallbackQueryHandler(ticker_binance_choice, pattern='^ps1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(ticker_bittrex_choice, pattern='^ps2$'))

updater.dispatcher.add_handler(CallbackQueryHandler(ticker_binance_choiced, pattern='^channel_binance_'))
updater.dispatcher.add_handler(CallbackQueryHandler(ticker_bittrex_choiced, pattern='^channel_bittrex_'))
#
#updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu3, pattern='^vs3$'))
#

conv_handler = ConversationHandler(
	#per_message = True,
	entry_points=[CallbackQueryHandler(reg_menu, pattern='register')],

	states={
		REGISTER: [MessageHandler(Filters.text,	channel_choice,	pass_user_data=True),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

conv_handler2 = ConversationHandler(
	#per_message = True,
	entry_points=[CallbackQueryHandler(default_msg, pattern='^default_'),
					CallbackQueryHandler(custom_msg, pattern='^custom_')],

	states={
		POST: [MessageHandler(Filters.text, post_submenu1),],
		#POST2: [MessageHandler(Filters.text, post_submenu2),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

conv_handler3 = ConversationHandler(
	#per_message = True,
	entry_points=[CallbackQueryHandler(view_editchannelname, pattern='^vs1_21', pass_user_data=True)],

	states={
		VIEW: [MessageHandler(Filters.text,	edit_channelname, pass_user_data=True),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)


conv_handler4 = ConversationHandler(
	#per_message = True,
	entry_points=[CallbackQueryHandler(view_editdefaultmessage, pattern='vs1_31')],

	states={
		VIEW_DEFAULTMESSAGE: [MessageHandler(Filters.text, edit_defaultmessage, pass_user_data=True),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

updater.dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(conv_handler2)
updater.dispatcher.add_handler(conv_handler3)
updater.dispatcher.add_handler(conv_handler4)
updater.dispatcher.add_error_handler(error)

# inline_caps_handler = InlineQueryHandler(inline_caps)
# updater.dispatcher.add_handler(inline_caps_handler)

updater.start_polling()
################################################################################