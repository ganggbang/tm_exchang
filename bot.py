#!/usr/bin/python3
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################
def start(bot, update):
	update.message.reply_text(main_menu_message(),
														reply_markup=main_menu_keyboard())

def about_menu(bot, update):
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
												message_id=query.message.message_id,
												reply_markup=about_menu_keyboard(),
												text=about_menu_message())

def reg_menu(bot, menu):
#Welcome, your 7-day FREE trial begins once you've entered your Channel's channelID	
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
												message_id=query.message.message_id,
												text=reg_menu_message(),)	
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
	print('activepos')
	query = update.callback_query
	bot.edit_message_text(chat_id=query.message.chat_id,
												message_id=query.message.message_id,
												text=activepos_menu_message(),
												reply_markup=activepos_menu_keyboard())

def closeorders_menu(bot, update):
	print('closeor')
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
def welcome_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Register', callback_data='register')],]
	return InlineKeyboardMarkup(keyboard)

def about_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Main menu', callback_data='main')],]
	return InlineKeyboardMarkup(keyboard)

def main_menu_keyboard():
	keyboard = [[InlineKeyboardButton('About', callback_data='about')],
							[InlineKeyboardButton('View', callback_data='m1')],
							[InlineKeyboardButton('Demo', callback_data='m2')],
							[InlineKeyboardButton('Settings', callback_data='m3')],
							[InlineKeyboardButton('Actions', callback_data='m4')],
							[InlineKeyboardButton('Pay Membership', callback_data='m5')],]
	return InlineKeyboardMarkup(keyboard)


def view_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Registered Channels', callback_data='vs1')],
							[InlineKeyboardButton('Check Wallet Balance', callback_data='vs2')],
							[InlineKeyboardButton('Position History & Performance', callback_data='vs3')],
							[InlineKeyboardButton('Main menu', callback_data='main')],]
	return InlineKeyboardMarkup(keyboard)

def view_submenu1_keyboard():
	keyboard = [[InlineKeyboardButton('Disable', callback_data='m1_11')],
							[InlineKeyboardButton('Enable', callback_data='m1_12')],
							[InlineKeyboardButton('View menu', callback_data='m1')]]
	return InlineKeyboardMarkup(keyboard)

def view_submenu2_keyboard():
	keyboard = [[InlineKeyboardButton('Bittrex', callback_data='m1_21')],
							[InlineKeyboardButton('Binance', callback_data='m1_22')],
							[InlineKeyboardButton('View menu', callback_data='m1')]]
	return InlineKeyboardMarkup(keyboard)

def view_submenu3_keyboard():
	keyboard = [[InlineKeyboardButton('All Channels', callback_data='m1_31')],
							[InlineKeyboardButton('Individual Channel', callback_data='m1_32')],
							[InlineKeyboardButton('View menu', callback_data='m1')]]
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
							[InlineKeyboardButton('Settings menu', callback_data='m3')]]
	return InlineKeyboardMarkup(keyboard)

def settings_submenu2_keyboard():
	keyboard = [[InlineKeyboardButton('Yes', callback_data='ss2_1')],
							[InlineKeyboardButton('No', callback_data='ss2_2')],
							[InlineKeyboardButton('Settings menu', callback_data='m3')]]
	return InlineKeyboardMarkup(keyboard)

def settings_submenu3_keyboard():
	keyboard = [[InlineKeyboardButton('Position Size', callback_data='ss3_1')],
							[InlineKeyboardButton('Spread Percent', callback_data='ss3_2')],
							[InlineKeyboardButton('Take Profit', callback_data='ss3_2')],
							[InlineKeyboardButton('Stop Loss', callback_data='ss3_3')],
							[InlineKeyboardButton('Trigger (Hidden)', callback_data='ss3_4')],
							[InlineKeyboardButton('Settings menu', callback_data='m3')]]
	return InlineKeyboardMarkup(keyboard)

def actions_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Offline Broadcast (Demo only)', callback_data='as1')],
							[InlineKeyboardButton('Select Channel', callback_data='as2')],
							[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)

def actions_submenu1_keyboard():
	keyboard = [[InlineKeyboardButton('Bittrex', callback_data='am1_11')],
							[InlineKeyboardButton('Binance', callback_data='am1_12')],
							[InlineKeyboardButton('Actions menu', callback_data='as2')]]
	return InlineKeyboardMarkup(keyboard)

def actions_submenu2_keyboard():
	keyboard = [[InlineKeyboardButton('Active Positions', callback_data='am2_11')],
							[InlineKeyboardButton('Close Active Orders', callback_data='am2_12')],
							[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)

def activepos_menu_keyboard():
	keyboard = [[InlineKeyboardButton('View Active Positions', callback_data='ap1_11')],
							[InlineKeyboardButton('Cancel Active Orders', callback_data='ap1_12')],
							[InlineKeyboardButton('Back', callback_data='as2')]]
	return InlineKeyboardMarkup(keyboard)

def closeorders_menu_keyboard():
	keyboard = [[InlineKeyboardButton('All Orders', callback_data='ap2_11')],
							[InlineKeyboardButton('Select Orders', callback_data='ap2_12')],
							[InlineKeyboardButton('Close Winners', callback_data='ap2_13')],
							[InlineKeyboardButton('Close Losses', callback_data='ap2_14')],
							[InlineKeyboardButton('Back', callback_data='as2')]]
	return InlineKeyboardMarkup(keyboard)


def pay_menu_keyboard():
	keyboard = [[InlineKeyboardButton('New Channel', callback_data='m5_1')],
							[InlineKeyboardButton('Renew', callback_data='m5_2')],
							[InlineKeyboardButton('Main menu', callback_data='main')]]
	return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def reg_menu_message():
	return 'Welcome, your 7-day FREE trial begins once you\'ve entered your Channel\'s channelID'

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
	return ''

def view_submenu1_message():
	return ''

def view_submenu2_message():
	return ''

def view_submenu3_message():
	return ''

def demo_menu_message():
	return 'Entering demo mode will assign random variables, connection to your exchange will be currently disabled, to turn off demo mode, head back into demo setting and choose off. Do you wish to continue?'

def demo_submenu_message():
	return ''	

def settings_menu_message():
	return ''

def settings_submenu1_message():
	return ''

def settings_submenu2_message():
	return ''

def settings_submenu3_message():
	return ''

def actions_menu_message():
	return ''

def actions_submenu1_message():
	return ''	

def actions_submenu2_message():
	return ''	

def pay_menu_message():
	return ''

def pay_submenu_message():
	return ''	

def activepos_menu_message():
	return ''

def closeorders_menu_message():
	return ''

############################# Handlers #########################################
updater = Updater('637840473:AAHi-_WkFXq8kTXSQyUR7dw5arDxW0Zaje4')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(about_menu, pattern='about'))
updater.dispatcher.add_handler(CallbackQueryHandler(reg_menu, pattern='register'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu1, pattern='vs1'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu2, pattern='vs2'))
updater.dispatcher.add_handler(CallbackQueryHandler(view_submenu3, pattern='vs3'))
updater.dispatcher.add_handler(CallbackQueryHandler(demo_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_menu, pattern='m3'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_submenu1, pattern='ss1'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_submenu2, pattern='ss2'))
updater.dispatcher.add_handler(CallbackQueryHandler(settings_submenu3, pattern='ss3'))
updater.dispatcher.add_handler(CallbackQueryHandler(actions_menu, pattern='m4'))
updater.dispatcher.add_handler(CallbackQueryHandler(actions_submenu1, pattern='as1'))
updater.dispatcher.add_handler(CallbackQueryHandler(actions_submenu2, pattern='as2'))

updater.dispatcher.add_handler(CallbackQueryHandler(activepos_menu, pattern='am2_11'))
updater.dispatcher.add_handler(CallbackQueryHandler(closeorders_menu, pattern='am2_12'))
#am2_11
updater.dispatcher.add_handler(CallbackQueryHandler(pay_menu, pattern='m5'))
#updater.dispatcher.add_handler(CallbackQueryHandler(pay_submenu, pattern='m5_1'))

updater.start_polling()
################################################################################