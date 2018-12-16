#!/usr/bin/python3
from user import *
import datetime
from dateutil import relativedelta
from dateutil import parser
import logging
from binance_exchange import *
from bittrex_exchange import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler,
						  ConversationHandler)
############################### Bot ############################################


def start(bot, update):
	checkuser(update)
	update.message.reply_text(main_menu_message(), reply_markup=main_menu_keyboard())


def about_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		reply_markup=about_menu_keyboard(),
		text=about_menu_message())


def reg_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Please type ChannelID",
		reply_markup=reg_menu_keyboard())


def pastein_menu(bot, update):
	query = update.callback_query

	bot.send_message(chat_id=query.message.chat_id,
		text="Please type ChannelID")
	return PASTEIN


def main_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=main_menu_message(),
		reply_markup=main_menu_keyboard())


def view_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id,
		text=view_menu_message(), reply_markup=view_menu_keyboard())


def view_submenu1(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
	 	message_id=query.message.message_id,
	 	text=view_submenu1_message(),
	 	reply_markup=view_submenu1_keyboard(query.message.chat_id))


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


def select_channels_menu(bot, update):
	query = update.callback_query
	channels = getchannels()
	keyboard = []

	for ch in channels:
		if ch['is_enable'] == 1:
			keyboard.append([InlineKeyboardButton(ch['channel_name'], callback_data='as2_1'+str(ch['id']))])
		else:
			keyboard.append([InlineKeyboardButton('* '+ch['channel_name'], callback_data='as2_1'+str(ch['id']))])
	keyboard.append([InlineKeyboardButton('Actions menu', callback_data='actions')])

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=select_channels_message(),
		reply_markup=InlineKeyboardMarkup(keyboard))


def actionchannels_menu(bot, update):
	query = update.callback_query

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=actionchannels_message(),
		reply_markup=actionchannels_keyboard(query['data'].replace('as2_1', '')))


def registredchannels_menu(bot, update):
	query = update.callback_query
#	print(query['data'])
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=registeredchannels_message(),
		reply_markup=registeredchannels_keyboard(query['data']))


def allchannels_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=allchannels_message(),
		reply_markup=allchannels_keyboard())	


def view_individual_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=view_individual_message(),
		reply_markup=view_individual_keyboard())	


def demo_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=demo_menu_message(),
		reply_markup=demo_menu_keyboard())


def demo_submenu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=demo_submenu_message(),
		reply_markup=demo_submenu_keyboard())


def settings_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=settings_menu_message(),
		reply_markup=settings_menu_keyboard())


def possize_menu(bot, update):
	query = update.callback_query

	bot.send_message(chat_id=query.message.chat_id,
		text="Position size is the amount of BTC used per trade, we recommend using anywhere from 3-5% of total account to mitigate risk")		
	return POS_SIZE


def spread_menu(bot, update):
	query = update.callback_query

	bot.send_message(chat_id=query.message.chat_id,
		text="The spread percent is a percentage added to bid price to increase chance of being executed. A response of '2.5' will add 2.5% to the bid price I.E: if current market price is $100 it will set the bid at $102.5")
	return SPREAD


def proffit_menu(bot, update):
	query = update.callback_query

	bot.send_message(chat_id=query.message.chat_id,
		text="Take profit is the price at which you want the trade to close at a profit, this is entered as a percentage that is added to the bid price executed. I.E: a response of '30', for an order executed at $100 will set a take profit at $130\", like wise a response of '250' sets the take profit at $250 or 250%")
	return TAKE_PROFIT


def stoploss_menu(bot, update):
	query = update.callback_query

	bot.send_message(chat_id=query.message.chat_id,
		text="Stop loss is the price at which you want the trade to close at a loss, this is entered as a percentage that is subtracted to the bid price executed. I.E a reponse of '10' for an order executed at $100 will set the stop loss at $90, like wise a response of '80' sets the stop loss at $20 or -80%, valid responses range from 1-99")
	return STOP_LOSS


def trigger_menu(bot, update):
	query = update.callback_query

	bot.send_message(chat_id=query.message.chat_id,
		text="Hidden")
	return TRIGGER


def apikey_menu(bot, update):
	query = update.callback_query

	if query['data'] == 'ss1_1':
		bot.send_message(chat_id=query.message.chat_id,
			text="Please enter your Bittrex API key in format 'api_key:private_key' and include the semi-colon")
		return Bittrex_API
	else:
		bot.send_message(chat_id=query.message.chat_id,
			text="Please enter your Binance API key in format 'api_key:private_key' and include the semi-colon")		
		return Binance_API


def settings_submenu1(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=settings_submenu1_message(),
		reply_markup=settings_submenu1_keyboard())


def settings_submenu2(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=settings_submenu2_message(),
		reply_markup=settings_submenu2_keyboard())


def settings_submenu3(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=settings_submenu3_message(),
		reply_markup=settings_submenu3_keyboard())


def actions_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=actions_menu_message(),
		reply_markup=actions_menu_keyboard())


def actions_submenu1(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=actions_submenu1_message(),
		reply_markup=actions_submenu1_keyboard())


def actions_submenu2(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=actions_submenu2_message(),
		reply_markup=actions_submenu2_keyboard())


def activepos_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=activepos_menu_message(),
		reply_markup=activepos_menu_keyboard())


def closeorders_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=closeorders_menu_message(),
		reply_markup=closeorders_menu_keyboard())	


def pay_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=pay_menu_message(),
		reply_markup=pay_menu_keyboard())


def pay_submenu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=pay_submenu_message(),
		reply_markup=pay_submenu_keyboard())


############################ Keyboards #########################################
def demo_submenu_keyboard():
	keyboard = [[InlineKeyboardButton('Register', callback_data='')],]
	return InlineKeyboardMarkup(keyboard)


def pay_submenu_keyboard():
	keyboard = [[InlineKeyboardButton('Register', callback_data='')],]
	return InlineKeyboardMarkup(keyboard)


def welcome_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Register', callback_data='')],]
	return InlineKeyboardMarkup(keyboard)


def reg_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Demo', callback_data='demo_afterreg')],
				[InlineKeyboardButton('Paste in ChannelID', callback_data='paste_inchannelid')],
				[InlineKeyboardButton('Main menu', callback_data='main')],]
	return InlineKeyboardMarkup(keyboard)


def about_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Main menu', callback_data='main')],]
	return InlineKeyboardMarkup(keyboard)


def active_positions_keyboard(channel_id):
	keyboard = [[InlineKeyboardButton('View Active Positions', callback_data='viewactivepos_'+str(channel_id))],
				[InlineKeyboardButton('Cancel Active Orders', callback_data='cancelactionsorders_'+str(channel_id))],
		[InlineKeyboardButton('Actions', callback_data='actions')],]
	return InlineKeyboardMarkup(keyboard)


def main_menu_keyboard():
	keyboard = [[InlineKeyboardButton('About', callback_data='about')],
			[InlineKeyboardButton('View', callback_data='view')],
			[InlineKeyboardButton('Register', callback_data='register')],
			[InlineKeyboardButton('Demo', callback_data='demo')],
			[InlineKeyboardButton('Settings', callback_data='settings')],
			[InlineKeyboardButton('Actions', callback_data='actions')],
			[InlineKeyboardButton('Pay Membership', callback_data='pay')],]
	return InlineKeyboardMarkup(keyboard)


def view_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Registered Channels', callback_data='vs1')],
			[InlineKeyboardButton('Check Wallet Balance', callback_data='vs2')],
			[InlineKeyboardButton('Position History & Performance', callback_data='vs3')],
			[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)


def actionchannels_keyboard(channel_id):
	keyboard = [[InlineKeyboardButton('Active Positions', callback_data='active_'+str(channel_id))],
			[InlineKeyboardButton('Close Active Orders', callback_data='closeactive_'+str(channel_id))],
			[InlineKeyboardButton('Actions menu', callback_data='actions')]]
	return InlineKeyboardMarkup(keyboard)	


def registeredchannels_keyboard(channel_id):
	keyboard = [[InlineKeyboardButton('Disable', callback_data='disable_'+str(channel_id))],
			[InlineKeyboardButton('Enable', callback_data='enable_'+str(channel_id))],
			[InlineKeyboardButton('Disable All', callback_data='disable_all')],
			[InlineKeyboardButton('View menu', callback_data='view')],]
	return InlineKeyboardMarkup(keyboard)	


def allchannels_keyboard():
	keyboard = [[InlineKeyboardButton('Best Channel', callback_data='vs1_51')],
			[InlineKeyboardButton('Worst Channel', callback_data='vs1_52')],
			[InlineKeyboardButton('Best Play', callback_data='vs1_53')],
			[InlineKeyboardButton('Worst Play', callback_data='vs1_54')],
			[InlineKeyboardButton('View menu', callback_data='view')],]
	return InlineKeyboardMarkup(keyboard)


def view_individual_keyboard():
	keyboard = [[InlineKeyboardButton('Last Position', callback_data='vs1_41')],
			[InlineKeyboardButton('Last Five', callback_data='vs1_42')],
			[InlineKeyboardButton('Weekly Perfomance', callback_data='vs1_43')],
			[InlineKeyboardButton('Best Play', callback_data='vs1_44')],
			[InlineKeyboardButton('Worst Play', callback_data='vs1_45')],
			[InlineKeyboardButton('Main menu', callback_data='view')],]
	return InlineKeyboardMarkup(keyboard)


def view_submenu1_keyboard(user_id):
	channels = getchannels(user_id)
	print(channels)
	d = []
	for ch in channels:
		d.append(str(ch['id']))

	using_channels = getusingchannels(d, user_id)
	print(using_channels)

	keyboard = []
	i = 1
	for ch in channels:
		if ch['id'] in using_channels:
			keyboard.append([InlineKeyboardButton('* '+ch['channel_name'], callback_data='vs1_1'+str(ch['id']))])
		else:
			keyboard.append([InlineKeyboardButton(ch['channel_name'], callback_data='vs1_1'+str(ch['id']))])
	keyboard.append([InlineKeyboardButton('View menu', callback_data='view')])

	return InlineKeyboardMarkup(keyboard)


def view_submenu2_keyboard():
	keyboard = [[InlineKeyboardButton('Bittrex', callback_data='vs1_21')],
			[InlineKeyboardButton('Binance', callback_data='vs1_22')],
			[InlineKeyboardButton('Both', callback_data='vs1_23')],			
			[InlineKeyboardButton('View menu', callback_data='view')]]
	return InlineKeyboardMarkup(keyboard)


def view_submenu3_keyboard():
	keyboard = [[InlineKeyboardButton('All Channels', callback_data='vs1_31')],
			[InlineKeyboardButton('Individual Channel', callback_data='vs1_32')],
			[InlineKeyboardButton('View menu', callback_data='view')]]
	return InlineKeyboardMarkup(keyboard)


def demo_menu_keyboard():
	keyboard = [[InlineKeyboardButton('ON', callback_data='m2_1')],
			[InlineKeyboardButton('OFF', callback_data='m2_2')],
			[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)


def settings_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Connect Exchange', callback_data='ss1')],
			[InlineKeyboardButton('Automation', callback_data='ss2')],
			[InlineKeyboardButton('Risk Settings', callback_data='ss3')],
			[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)


def settings_submenu1_keyboard():
	keyboard = [[InlineKeyboardButton('Bittrex API', callback_data='ss1_1')],
			[InlineKeyboardButton('Binance API', callback_data='ss1_2')],
			[InlineKeyboardButton('Settings menu', callback_data='settings')]]
	return InlineKeyboardMarkup(keyboard)


def settings_submenu2_keyboard():
	keyboard = [[InlineKeyboardButton('Yes', callback_data='ss2_1')],
			[InlineKeyboardButton('No', callback_data='ss2_2')],
			[InlineKeyboardButton('Settings menu', callback_data='settings')]]
	return InlineKeyboardMarkup(keyboard)


def settings_submenu3_keyboard():
	keyboard = [[InlineKeyboardButton('Position Size', callback_data='ss3_1')],
			[InlineKeyboardButton('Spread Percent', callback_data='ss3_2')],
			[InlineKeyboardButton('Take Profit', callback_data='ss3_3')],
			[InlineKeyboardButton('Stop Loss', callback_data='ss3_4')],
			[InlineKeyboardButton('Trigger (Hidden)', callback_data='ss3_5')],
			[InlineKeyboardButton('Settings menu', callback_data='settings')]]
	return InlineKeyboardMarkup(keyboard)


def actions_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Offline Broadcast (Demo only)', callback_data='as1')],
			[InlineKeyboardButton('Select Channel', callback_data='as2')],
			[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)


def actions_submenu1_keyboard():
	keyboard = [[InlineKeyboardButton('Bittrex', callback_data='am1_11')],
			[InlineKeyboardButton('Binance', callback_data='am1_12')],
			[InlineKeyboardButton('Actions menu', callback_data='actions')]]
	return InlineKeyboardMarkup(keyboard)


def actions_submenu2_keyboard():
	keyboard = [[InlineKeyboardButton('Active Positions', callback_data='am2_11')],
			[InlineKeyboardButton('Close Active Orders', callback_data='am2_12')],
			[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)


def activepos_menu_keyboard():
	keyboard = [[InlineKeyboardButton('View Active Positions', callback_data='ap1_11')],
			[InlineKeyboardButton('Cancel Active Orders', callback_data='ap1_12')],
			[InlineKeyboardButton('Back', callback_data='actions')]]
	return InlineKeyboardMarkup(keyboard)


def closeorders_menu_keyboard():
	keyboard = [[InlineKeyboardButton('All Orders', callback_data='ap2_11')],
			[InlineKeyboardButton('Select Orders', callback_data='ap2_12')],
			[InlineKeyboardButton('Close Winners', callback_data='ap2_13')],
			[InlineKeyboardButton('Close Losses', callback_data='ap2_14')],
			[InlineKeyboardButton('Back', callback_data='actions')]]
	return InlineKeyboardMarkup(keyboard)


def pay_menu_keyboard():
	keyboard = [[InlineKeyboardButton('New Channel', callback_data='pay_1')],
			[InlineKeyboardButton('Renew', callback_data='pay_2')],
			[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
# def reg_menu_message():
# 	return 'Welcome, your 7-day FREE trial begins once you\'ve entered your Channel\'s channelID'


def about_menu_message():
	return 'JanusBot is a tool for users to execute trade opportunities live sent by the channels their invested in without the need of leaving Telegram. By default, and for risk purposes dictated by the user\
		we have the automation option turned off. To turn on automated orders, or the ability for the bot to execute orders for you the second they\'re sent out by channels, head over to Settings > Automation. An advantage of\
		Janus is that it will send you live trade opportunities from all your channels the moment they happen, giving the user the ability to choose whether or not to execute them with a single click. If you have more than\
		one channel, Janus gives you the option of disabling some channels, with the option of renabling them later. Other commands Janus can do is check performance of individual channels or compare results of\
		all the channels. As well as the ability to view any active orders, and either cancel them, close them, or close just the winners or losers. Janus works with a preset risk strategy set by the user in the settings. Such options\
		include positional size per play, spread percent, take profit, and stop loss. Since these tools aren\'t native in Bittrex or Binance, Janus uses triggers to switch orders from a take profit order to a stop loss if the price falls below\
		a certain threshold. Janus is constantly being updated for bugs, new features, and performance.'

def welcome_menu_message():
	return 'Welcome to Janus, start by registering to gain access.'


def main_menu_message():
	return 'Welcome to Janus, start by registering to gain access.'


def view_menu_message():
	return 'Choose the option in menu:'


def view_submenu1_message():
	return 'Choose the option in menu:'


def view_submenu2_message():
	return 'Choose the option in menu:'


def view_submenu3_message():
	return 'Choose the option in menu:'


def demo_menu_message():
	return 'Entering demo mode will assign random variables, connection to your exchange will be currently disabled, to turn off demo mode, head back into demo setting and choose off. Do you wish to continue?'


def demo_submenu_message():
	return 'Choose the option in menu:'	


def settings_menu_message():
	return 'Choose the option in menu:'


def settings_submenu1_message():
	return 'Choose the option in menu:'


def settings_submenu2_message():
	return 'Choose the option in menu:'


def settings_submenu3_message():
	return 'Choose the option in menu:'


def actions_menu_message():
	return 'Choose the option in menu:'


def actions_submenu1_message():
	return 'Choose the option in menu:'	


def actions_submenu2_message():
	return 'Choose the option in menu:'	


def pay_menu_message():
	return 'Choose the option in menu:'


def pay_submenu_message():
	return 'Choose the option in menu:'	


def activepos_menu_message():
	return 'Choose the option in menu:'


def closeorders_menu_message():
	return 'Choose the option in menu:'


def allchannels_message():
	return 'Choose the option in menu:'


def actionchannels_message():
	return 'Choose the option in menu:'


def select_channels_message():
	return 'Choose the channel in menu:'


def registeredchannels_message():
	return 'Choose the channel in menu:'


def view_individual_message():
	return 'Choose the option in menu:'


def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)


def pay_newchannel(bot, update):
	print('new')
	return False


def pay_renew(bot, update):
	print('renew')
	return False	


def done(update):

	update.message.reply_text(""
							  "{}"
							  "Until next time!")

	return ConversationHandler.END


def bittrex_api_choice(bot, update):
	text = update.message.text

	user_id = update['message']['chat']['id']
	setBittrexAPI(text, user_id)

	update.message.reply_text('Your {} API has been successfully added'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def binance_api_choice(bot, update):
	text = update.message.text

	user_id = update['message']['chat']['id']
	setBinanceAPI(text, user_id)
	update.message.reply_text('Your {} API has been successfully added'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def pos_size_choice(bot, update):
	text = update.message.text

	user_id = update['message']['chat']['id']
	set_position_size_per(text, user_id)
	update.message.reply_text('Position Size {} saved'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def spread_choice(bot, update):
	text = update.message.text
	user_id = update['message']['chat']['id']
	set_spread_percent(text, user_id)
	update.message.reply_text('Spread Percent {} saved'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def proffit_choice(bot, update):
	text = update.message.text
	user_id = update['message']['chat']['id']
	set_take_profit(text, user_id)
	update.message.reply_text('Take Profit {} saved'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def stoploss_choice(bot, update):
	text = update.message.text
	user_id = update['message']['chat']['id']
	setStopLoss(text, user_id)
	update.message.reply_text('Stop Loss {} saved'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def pastein_choise(bot, update):
	text = update.message.text

	user_id = update['message']['chat']['id']
	pasteinchannels(text, user_id)

	update.message.reply_text('Channel {} successfully registered!'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def trigger_choice(bot, update):
	text = update.message.text

	user_id = update['message']['chat']['id']
	setTrigger(text, user_id)
	update.message.reply_text('Trigger {} saved'.format(text.lower()),
		reply_markup=main_menu_keyboard())

	return ConversationHandler.END


def action_demoon(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="User currently in demo-mode, random variables have been assigned. To act as the broadcaster, head over to Actions > Offline Broadcast, this will mimic the action of receiving a broadcasted ticker by your channel. To exit demo return to the demo menu option and select OFF",
		reply_markup=main_menu_keyboard())
	DemoOn(query.message.chat_id)


def action_demooff(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Demo mode has been exited",
		reply_markup=main_menu_keyboard())
	DemoOff(query.message.chat_id)


def action_autoon(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="All incoming ticker broadcasts will be automatically executed",
		reply_markup=main_menu_keyboard())
	AutomationOn(query.message.chat_id)


def action_autooff(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Trade suggestion declined",
		reply_markup=main_menu_keyboard())

	AutomationOff(query.message.chat_id)


def bittrex_bal(user_id):

	text = '**Bittrex** '
	balances = bittrex_getbalances(user_id)
	for balance in balances['result']:
		if balance['Balance'] > 0:
			text += balance['Currency'] + ': ' + str(balance['Balance']) + ' Available: ' + str(
				balance['Available']) + '\n'
	return text


def bittrex_bal_menu(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	try:
		text = bittrex_bal(chat_id)

		bot.edit_message_text(chat_id=chat_id,
			message_id=query.message.message_id,
			text=text,
			reply_markup=main_menu_keyboard())	
	except Exception as e:
		bot.edit_message_text(chat_id=chat_id,
			message_id=query.message.message_id,
			text=str(e)+"",
			reply_markup=main_menu_keyboard())	


def binance_bal(user_id):
	balances = binance_getbalances(user_id)

	text = '**Binance** '
	for balance in balances['balances']:
		if float(balance['free']) > 0:
			text += balance['asset'] + ': ' + str(balance['free']) + ' Available: ' + str(
				balance['free']) + '\n'

	return text


def binance_bal_menu(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	try:
		text = binance_bal(chat_id)
		bot.edit_message_text(chat_id=chat_id,
			message_id=query.message.message_id,
			text = text,
			reply_markup=main_menu_keyboard())

	except Exception as e:
		bot.edit_message_text(chat_id=chat_id,
			message_id=query.message.message_id,
			reply_markup=main_menu_keyboard(),
			text=str(e)+"")


def both_bal(bot, update):
	query = update.callback_query

	text = bittrex_bal(query.message.chat_id)
	text += binance_bal(query.message.chat_id)

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text=text,
		reply_markup=main_menu_keyboard())


def enable_channel(bot, update):
	query = update.callback_query
	channel_id = query['data']
	user_id = query.message.chat_id

	enable_channelsql(channel_id.replace('enable_vs1_1', ''), user_id)
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id = query.message.message_id,
		text  ="Selected channel have been enabled",
		reply_markup = main_menu_keyboard())


def disable_allchannel(bot, update):
	query = update.callback_query
	#channel_id = query['data']
	user_id = query.message.chat_id

	disable_allchannelsql(user_id)
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Disabled ALL channels",
		reply_markup=main_menu_keyboard())


def disable_channel(bot, update):
	query = update.callback_query
	channel_id = query['data']
	user_id = query.message.chat_id

	disable_channelsql(channel_id.replace('disable_vs1_1', ''),  user_id)
	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Selected channel have been disabled",
		reply_markup=main_menu_keyboard())


def cancelorder(chat_id, order):
	if order['exchange'].upper() == 'BITTREX':
		result = bittrex_cancel(chat_id, uuid=order['orderId'])
		#if result['success'] is True:
	elif order['exchange'].upper() == 'BINANCE':
		result = binancecancel_order(chat_id, symbol=order['ticker'], orderId=order['orderId'])
	#del_order(order['orderId'])
	cancel_order(order['orderId'])

	result['status'] = 'Canceled'
	return result


def cancelorder_menu(bot, update):
	query = update.callback_query
	query_data = query['data'].replace('cancelorder_', '')
	chat_id = query.message.chat_id

	# r = binance_get_all_orders(chat_id, symbol = 'NEOBTC')
	# bittrex_orders = bittrex_get_open_orders(chat_id, market='btc-neo')

	s = query_data.split('_')
	channel_id = s[0]
	orderId = s[1]

	if orderId.upper() == 'ALL':
		orders = get_orders(chat_id)
		for order in orders:
			result = cancelorder(chat_id, order)
	else:
		order = get_order(orderId)
		result = cancelorder(chat_id, order)

	keyboard = orders_keyboard(chat_id, channel_id)
	bot.edit_message_text(chat_id=chat_id,
		message_id=query.message.message_id,
		text="Selected orders have been "+result['status']+": ",
		reply_markup=keyboard)

def get_timeactive(chat_id, szDate, exchange):

	try:
		if exchange == 'BINANCE':
			server_time = binance_get_server_time(chat_id)
			t1 = datetime.datetime.fromtimestamp(szDate/1000)
			t2 = datetime.datetime.fromtimestamp(int(server_time['serverTime'])/1000)
		elif exchange == 'BITTREX':
			t1 = parser.parse(szDate)
			t2 = datetime.datetime.now()

		difference = relativedelta.relativedelta(t2, t1)
		days = difference.days
		hours = difference.hours
		minutes = difference.minutes
		return "Time Active: " + str(days) + " day, " + str(hours) + " hours, " + str(minutes) + " minutes : "
	except Exception as e:
		print(e)


def orders_keyboard(chat_id, channel_id):
	orders = get_orders(channel_id, chat_id)

	keyboard = []
	for order in orders:
		if order['exchange'].upper() == 'BINANCE':
			#binance_orders = binance_get_open_orders(chat_id, symbol=order['ticker'])
			binance_orders = binance_get_all_orders(chat_id, symbol=order['ticker'])

			for bin_order in binance_orders:
				if bin_order['status'] == 'NEW' and bin_order['orderId'] == int(order['orderId']):
					current_price = binance_get_symbol_ticker(chat_id, order['ticker'])
					keyboard.append([InlineKeyboardButton(order['ticker'] + ":BINANCE, Bid Price: $"+str(bin_order['price'])+", Current: $"+str(current_price)+", Current return: X%, "+get_timeactive(chat_id, bin_order['time'], "BINANCE"),
													  callback_data='cancelorder_' + str(channel_id) + '_' + str(bin_order['orderId']))])

		if order['exchange'].upper() == 'BITTREX':
			bittrex_orders = bittrex_get_open_orders(chat_id, market=order['ticker'])
			#bittrex_orders = bittrex_get_order_history(chat_id, market=order['ticker'])
			#bittrex_orders = bittrex_get_orderbook(chat_id, market=order['ticker'])

			if bittrex_orders['success'] is True:
				for bit_order in bittrex_orders['result']:
					if bit_order['OrderUuid'] == order['orderId']:
						current_price = bittrex_getticker(chat_id, market=order['ticker'])['result']['Ask']
						keyboard.append([InlineKeyboardButton(bit_order['Exchange']+":BITTREX, Bid Price: $"+str(bit_order['Limit'])+", Current: $"+str(current_price)+", Current return: X%, "+get_timeactive(chat_id, bit_order['Opened'], "BITTREX"), callback_data='cancelorder_'+str(channel_id)+'_'+str(bit_order['OrderUuid']))])

	keyboard.append([InlineKeyboardButton("Cancel ALL Orders", callback_data='cancelorder_'+str(channel_id)+'_all')])
	keyboard.append([InlineKeyboardButton("Actions Menu", callback_data='actions')])

	return InlineKeyboardMarkup(keyboard)


def viewactivepos(bot, update):
	query = update.callback_query
	channel_id = query['data'].replace('viewactivepos_', '').replace('cancelactionsorders_', '')
	chat_id = query.message.chat_id

	keyboard = orders_keyboard(chat_id, channel_id)
	bot.edit_message_text(chat_id=chat_id,
		message_id=query.message.message_id,
		text="Choose order for CANCEL: ",
		reply_markup=keyboard)


def active_positions_menu(bot, update):
	query = update.callback_query

	channel_id = query['data'].replace('active_','')
	#viewactive_positions(channel_id)

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Choose the option in menu: ",
		reply_markup=active_positions_keyboard(channel_id))

def offlinebr_menu(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id

	# r = bittrex_get_order_history(chat_id, market='BTC-NEO')
	#result = bittrex_cancel(api_key, api_secret, uuid=order['orderId'])

	#if result['success'] is True:
	# elif order['exchange'].upper() == 'BINANCE':

	#result = binance_get_my_trades(chat_id, symbol='NEOBTC')
	r = binance_get_all_orders(chat_id, symbol='NEOBTC')
	#


def closeactive_orders_keyboard(order_id):
	keyboard = [[InlineKeyboardButton('All Orders', callback_data='all_ordersclose')],
		[InlineKeyboardButton('Select Orders', callback_data='select_ordersclose_'+str(order_id))],
		[InlineKeyboardButton('Actions', callback_data='actions')],]
	return InlineKeyboardMarkup(keyboard)


def closeactive_orders_menu(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id
	channel_id = query['data'].replace('closeactive_','')

	orders = get_orders_by_filled(channel_id, chat_id)

	keyboard = []

	for order in orders:
		if order['exchange'].upper() == 'BITTREX':
			bittrex_orders = bittrex_get_order_history(chat_id, market='btc-neo'.upper())
			for bit_order in bittrex_orders['result']:
				if bit_order['Closed'] is not False and bit_order['OrderUuid'] == order['orderId']:
					current_price = bittrex_getticker(chat_id, market=order['ticker'])['result']['Ask']
					keyboard.append([InlineKeyboardButton(order['ticker'] + ":BITTREX, Bid Price: $" + str(
						bit_order['Price']) + ", Current: $" + str(
						current_price) + ", Current return: X%, " + get_timeactive(chat_id, bit_order['Closed'], "BITTREX"),
							callback_data='closeorder_' + str(channel_id) + '_' + str(bit_order['OrderUuid']))])

		elif order['exchange'].upper() == 'BINANCE':
			binance_orders = binance_get_all_orders(chat_id, symbol='NEOBTC')
			for bin_order in binance_orders:
				if bin_order['status'] == 'FILLED' and int(order['orderId']) == bin_order['orderId']:
					current_price = binance_get_symbol_ticker(chat_id, order['ticker'])
					keyboard.append([InlineKeyboardButton(order['ticker'] + ":BINANCE, Bid Price: $" + str(
						bin_order['price']) + ", Current: $" + str(
						current_price) + ", Current return: X%, " + get_timeactive(chat_id, bin_order['time'], "BINANCE"),
							callback_data='closeorder_' + str(channel_id) + '_' + str(bin_order['orderId']))])

	keyboard.append([InlineKeyboardButton("Close Winners", callback_data='closeorder_' + str(channel_id) + '_winners')])
	keyboard.append([InlineKeyboardButton("Close Losses", callback_data='closeorder_' + str(channel_id) + '_losses')])
	keyboard.append([InlineKeyboardButton("Close ALL Orders", callback_data='closeorder_' + str(channel_id) + '_all')])
	keyboard.append([InlineKeyboardButton("Actions Menu", callback_data='actions')])
	#closeactive_orders(order_id)

	bot.edit_message_text(chat_id=chat_id,
		message_id=query.message.message_id,
		text="Choose the option in menu:",
		reply_markup=InlineKeyboardMarkup(keyboard))


def orderclose(chat_id, order):
	if order['exchange'].upper() == 'BITTREX':
		current_price = bittrex_getticker(chat_id, market=order['ticker'])['result']['Ask']
		r = bittrex_sell_limit(chat_id, quantity=order['quantity'], market=order['ticker'], rate=current_price);
		if r['success'] is True:
			sell_order(order['orderId'])
	elif order['exchange'].upper() == 'BINANCE':
		current_price = binance_get_symbol_ticker(chat_id, symbol=order['ticker'])
		assets = binance_getbalances(chat_id)

		for asset in assets['balances']:
			if asset['asset'] == order['ticker'].replace('BTC', ''):  # TODO fixme!
				bal = asset['free']
				# trades = binance_get_recent_trades(chat_id, symbol=order['ticker'])
				# quantity = (float(bal))/(float(trades[0]['price'])) * 0.9995
				#diff = float(order['quantity']) - float(bal)
				#q = round(float(order['quantity']) - diff, 6)
				r = binance_order_limit_sell(chat_id, symbol=order['ticker'], quantity=order['quantity'], price=current_price)
				if r['status'] == 'FILLED':
					sell_order(order['orderId'])


def select_ordersclose_menu(bot, update):
	query = update.callback_query
	chat_id = query.message.chat_id
	query_data = query['data'].replace('closeorder_', '')

	s = query_data.split('_')
	channel_id = s[0]
	orderId = s[1]

	if orderId.upper() == 'ALL':
		orders = get_orders_by_filled(channel_id, chat_id)
		for order in orders:
			orderclose(order)
	elif orderId.upper() == 'WINNERS':#todo fix!
		orders = get_orders_by_filled(channel_id, chat_id)
		#for order in orders:
		#	orderclose(order)
	elif orderId.upper() == 'LOSSES':#todo fix!
		orders = get_orders_by_filled(channel_id, chat_id)
		#for order in orders:
		#	orderclose(order)
	else:
		order = get_order(channel_id, orderId)
		orderclose(order)

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Choose the option in menu:",
		reply_markup=main_menu_keyboard())


def paste_inchannelid(bot, update):
	query = update.callback_query

	bot.edit_message_text(chat_id=query.message.chat_id,
		message_id=query.message.message_id,
		text="Choose the option in menu:",
		reply_markup=main_menu_keyboard())


def is_per_or_amount(pos_size):
	if pos_size['pos_size_amount'] is not None and pos_size['pos_size_per'] is None:
		return float(pos_size['pos_size_amount'])
	elif pos_size['pos_size_amount'] is None and pos_size['pos_size_per'] is not None:
		return float(pos_size['pos_size_per'])


def broadcast_answer(bot, update):
	query = update.callback_query
	message_id = query['data'].replace('bmy_', '')
	chat_id = query.message.chat_id

	msg = getbroadcastmsgbyid(message_id)

	if is_settings(chat_id) is None:
		settings_submenu3(bot, update)
		return

	m = re.search(r"(.*):(.*)@(.*)", msg['message'])

	if m.group(0) and m.group(1) and m.group(2) and m.group(3):
		exchange = m.group(2)
		symbol = m.group(1).upper()
		price = m.group(3)

		pos_size = is_per_or_amount(get_position_size(chat_id))
		spread_size = get_spread_percent(chat_id)

		if exchange.upper() == 'BINANCE':
			balance = binance_getbalance(chat_id, 'BTC')['free']
			q = get_percentage(pos_size, balance)
			q = q / float(price)
			p = get_percentage(spread_size, price)
			price = float(price) + p
			result = binance_order_limit_buy(chat_id, symbol=symbol, side='BUY', price=price, quantity=q)
			#if result['orderId']:
			if isinstance(result, dict):
				insert_order(chat_id, symbol, 'BINANCE', result['orderId'])
				message = "Bid order has been placed for '" + str(m.group(1)).upper() + "':'" + str(
					m.group(2)).upper() + "' at '" + str(m.group(3)).upper() + "' BTC"
			else:
				message = result
		elif exchange.upper() == 'BITTREX':
			balance = bittrex_getbalance(chat_id, 'BTC')['result']['Available']
			q = get_percentage(pos_size, balance)
			q = q / float(price)
			p = get_percentage(spread_size, price)
			price = float(price) + p

			result = bittrex_buy_limit(chat_id, market=symbol, quantity=q, rate=price)
			if result['success'] is not True:
				message = result['message']
			else:
				message = "Bid order has been placed for '"+str(m.group(1)).upper()+"':'"+str(m.group(2)).upper()+"' at '"+str(m.group(3)).upper()+"' BTC"
				insert_order(chat_id, symbol, 'BITTREX', result['result']['uuid'])
		bot.edit_message_text(chat_id=chat_id,
							  message_id=query.message.message_id,
							  text=message,
							  reply_markup=main_menu_keyboard())


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

Bittrex_API, Binance_API, POS_SIZE, SPREAD, TAKE_PROFIT, STOP_LOSS, TRIGGER, PASTEIN = range(8)


############################# Handlers #########################################
updater = Updater(token='692136526:AAGbRDOH2uO35F6Em843eQDVLpiW6MFcLmk')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main$'))
updater.dispatcher.add_handler(CallbackQueryHandler(about_menu, pattern='about$'))
updater.dispatcher.add_handler(CallbackQueryHandler(reg_menu, pattern='^register$'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_menu, pattern='view$'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu1, pattern='^vs1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu2, pattern='^vs2$'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu3, pattern='^vs3$'))
updater.dispatcher.add_handler(CallbackQueryHandler(demo_menu, pattern='demo$'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_menu, pattern='settings$'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_submenu1, pattern='^ss1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_submenu2, pattern='^ss2$'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_submenu3, pattern='^ss3$'))
updater.dispatcher.add_handler(CallbackQueryHandler(actions_menu, pattern='actions$'))

updater.dispatcher.add_handler(CallbackQueryHandler(active_positions_menu, pattern='^active_'))
updater.dispatcher.add_handler(CallbackQueryHandler(cancelorder_menu, pattern='^cancelorder_'))
updater.dispatcher.add_handler(CallbackQueryHandler(viewactivepos, pattern='^cancelactionsorders_'))
updater.dispatcher.add_handler(CallbackQueryHandler(viewactivepos, pattern='^viewactivepos_'))

updater.dispatcher.add_handler(CallbackQueryHandler(action_demoon, pattern='m2_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(action_demooff, pattern='m2_2'))

updater.dispatcher.add_handler(CallbackQueryHandler(action_autoon, pattern='^ss2_1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(action_autooff, pattern='^ss2_2$'))

updater.dispatcher.add_handler(CallbackQueryHandler(closeactive_orders_menu, pattern='^closeactive_'))
updater.dispatcher.add_handler(CallbackQueryHandler(select_ordersclose_menu, pattern='^closeorder_'))

updater.dispatcher.add_handler(CallbackQueryHandler(registredchannels_menu, pattern='^vs1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(actionchannels_menu, pattern='^as2_1'))

updater.dispatcher.add_handler(CallbackQueryHandler(disable_allchannel, pattern='^disable_all$'))
updater.dispatcher.add_handler(CallbackQueryHandler(disable_channel, pattern='^disable_v'))
updater.dispatcher.add_handler(CallbackQueryHandler(enable_channel, pattern='^enable_'))

updater.dispatcher.add_handler(CallbackQueryHandler(broadcast_answer, pattern='^bmy_'))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='^bmn_'))
#bmn_

updater.dispatcher.add_handler(CallbackQueryHandler(offlinebr_menu, pattern='^as1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(select_channels_menu, pattern='^as2$'))

updater.dispatcher.add_handler(CallbackQueryHandler(allchannels_menu, pattern='vs1_31'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_individual_menu, pattern='vs1_32'))

updater.dispatcher.add_handler(CallbackQueryHandler(activepos_menu, pattern='am2_11'))
updater.dispatcher.add_handler(CallbackQueryHandler(closeorders_menu, pattern='am2_12'))
#am2_11
updater.dispatcher.add_handler(CallbackQueryHandler(pay_menu, pattern='^pay$'))
updater.dispatcher.add_handler(CallbackQueryHandler(pay_newchannel, pattern='^pay_1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(pay_renew, pattern='^pay_2$'))

updater.dispatcher.add_handler(CallbackQueryHandler(bittrex_bal_menu, pattern='vs1_21'))
updater.dispatcher.add_handler(CallbackQueryHandler(binance_bal_menu, pattern='vs1_22'))
updater.dispatcher.add_handler(CallbackQueryHandler(both_bal, pattern='vs1_23'))
#updater.dispatcher.add_handler(CallbackQueryHandler(pay_submenu, pattern='m5_1'))

updater.dispatcher.add_error_handler(error)


conv_handler = ConversationHandler(
	#per_message = True,
	entry_points=[CallbackQueryHandler(apikey_menu, pattern='^ss1_1$'), 
				CallbackQueryHandler(apikey_menu, pattern='^ss1_2$')],

	states={
		Bittrex_API: [MessageHandler(Filters.text,	bittrex_api_choice),],
		Binance_API: [MessageHandler(Filters.text,	binance_api_choice),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

conv_handler2 = ConversationHandler(
	entry_points=[CallbackQueryHandler(possize_menu, pattern='^ss3_1$'),],

	states={
		POS_SIZE: [MessageHandler(Filters.text,	pos_size_choice),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)
#
conv_handler3 = ConversationHandler(
	entry_points=[CallbackQueryHandler(spread_menu, pattern='^ss3_2$'),],

	states={
		SPREAD: [MessageHandler(Filters.text, spread_choice),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

conv_handler4 = ConversationHandler(
	entry_points=[CallbackQueryHandler(proffit_menu, pattern='^ss3_3$'),],

	states={
		TAKE_PROFIT: [MessageHandler(Filters.text, proffit_choice),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

conv_handler5 = ConversationHandler(
	entry_points=[CallbackQueryHandler(stoploss_menu, pattern='^ss3_4$'),],

	states={
		STOP_LOSS: [MessageHandler(Filters.text, stoploss_choice),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

conv_handler6 = ConversationHandler(
	entry_points=[CallbackQueryHandler(trigger_menu, pattern='^ss3_5$'),],

	states={
		TRIGGER: [MessageHandler(Filters.text, trigger_choice),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

conv_handler7 = ConversationHandler(
	entry_points=[CallbackQueryHandler(pastein_menu, pattern='paste_inchannelid'),],

	states={
		PASTEIN: [MessageHandler(Filters.text, pastein_choise),],
	},

	fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
)

updater.dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(conv_handler2)
updater.dispatcher.add_handler(conv_handler3)
updater.dispatcher.add_handler(conv_handler4)
updater.dispatcher.add_handler(conv_handler5)
updater.dispatcher.add_handler(conv_handler6)
updater.dispatcher.add_handler(conv_handler7)

updater.start_polling()
################################################################################