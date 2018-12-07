import pymysql
import re
import json
from connection import create_connection, save

def del_order(orderId):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "DELETE FROM `orders` WHERE `orderId` = '"+str(orderId)+"'"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def get_order(orderId):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `ticker`,`exchange`, `last_active`, `orderId` FROM `orders` WHERE `orderId` = '"+str(orderId)+"'")

	order = cursor.fetchone()

	connection.close()
	return order


def get_orders(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `ticker`,`exchange`, `last_active`, `orderId` FROM `orders` WHERE `tm_id` = "+str(user_id))

	tickers = []
	for t in cursor.fetchall():
		tickers.append(t)
	connection.close()
	return tickers

def insert_order(user_id, ticker, exchange, orderId):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "INSERT INTO `orders`(`tm_id`, `ticker`, `exchange`, `orderId`,`last_active`) VALUES ("+str(user_id)+", '"+ticker+"', '"+exchange+"', '"+str(orderId)+"', NOW())"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def getbroadcastmsgbyid(message_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `message` FROM `broadcasting_msg` WHERE `id` = "+str(message_id))

	message = cursor.fetchone()
	connection.close()
	return message


def setbroadcastmessages_sended(message_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `broadcasting_msg` SET `is_sended`=1, `changed` = NOW() WHERE `id` = "+str(message_id)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	connection.close()


def getbroadcastmessages():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `message`,`tm_id`,`id` FROM `broadcasting_msg` WHERE `is_sended` = 0")

	messages = []
	for ch in cursor.fetchall():
		messages.append(ch)
	connection.close()
	return messages


def pasteinchannels(channel_id, user_id):
	connection = create_connection()
	connection.close()

def ordersclose(order_id):
	connection = create_connection()
	connection.close()

def all_ordersclose():
	connection = create_connection()
	connection.close()

def viewactive_positions(user_id):
	connection = create_connection()
	connection.close()

def closeactive_orders(user_id):
	connection = create_connection()
	connection.close()

def disable_allchannelsql(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `using_channels` SET `is_enable`= 0 WHERE `user_id` = "+str(user_id)
	print(sql)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	connection.close()

def disable_channelsql(channel_id, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `using_channels` SET `is_enable`= 0 WHERE `channel_id` = "+str(channel_id)+" AND `user_id` = "+str(user_id)
	print(sql)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	connection.close()

def enable_channelsql(channel_id, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `using_channels` SET `is_enable`= 1 WHERE `channel_id` = "+str(channel_id)+" AND `user_id` = "+str(user_id)
	print(sql)	
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	connection.close()

def getusingchannels(channels, user_id):
	szchannels = ", ".join(channels)
	dict_channels = []

	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	
	if szchannels:
		sql = "SELECT `channel_name`, `channel_id`, `id`, `is_enable` FROM `using_channels` WHERE `channel_id` IN ("+szchannels+") AND `user_id` = "+str(user_id)+" AND `is_enable` = 1"
		#sql = "SELECT `channel_name`, `id`, `is_enable` FROM `channels` WHERE `id` IN ("+szchannels+")"
		print(sql)
		cursor.execute(sql)

		for ch in cursor.fetchall():
			dict_channels.append(ch['channel_id'])

	connection.close()

	return dict_channels


def getticker_channel(channel_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `ticker` FROM `channels` WHERE `is_enable` = 1 AND `id` = "+str(channel_id))

	ticker = cursor.fetchone()
	connection.close()
	return ticker


def getchannels():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	#cursor.execute("SELECT `channel_name`, `id`, `is_enable` FROM `using_channels` WHERE `user_id` = "+str(user_id))
	cursor.execute("SELECT `channel_name`, `id`, `is_enable` FROM `channels` WHERE `is_enable` = 1")

	channels = []
	for ch in cursor.fetchall():
		channels.append(ch)
	connection.close()

	return channels

def checkuser(update):
	user_id = update['message']['chat']['id']
	user = {
		"tm_id": update['message']['chat']['id'],
		"first_name": update['message']['chat']['first_name'],
		"last_name": update['message']['chat']['last_name'],
		"username": update['message']['chat']['username']
	}

	if existing_user(user_id) is False:
		connection = create_connection()
		save(connection, 'users', user)
		connection.close()

def existing_user(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `tm_id` FROM `users` WHERE `tm_id` = "+str(user_id))
	user_id = cursor.fetchone()
	connection.close()

	if user_id:
		return True
	return False

def isDemo(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `tm_id` FROM `users` WHERE `is_demo` = 1 AND `tm_id` = "+str(user_id))
	user_id = cursor.fetchone()

	connection.close()

	if user_id:
		return True
	return False

def AutomationOn(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `users` SET `is_demo`= 1 WHERE `tm_id` = "+str(user_id)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	connection.close()
	
def AutomationOff(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `users` SET `is_automation`= 0 WHERE `tm_id` = "+str(user_id)
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def DemoOn(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `users` SET `is_automation`= 1 WHERE `tm_id` = "+str(user_id)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	connection.close()
	
def DemoOff(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `users` SET `is_demo`= 0 WHERE `tm_id` = "+str(user_id)
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def setBittrexAPI(api, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `users` SET `bittrex_api`= '"+api.trim()+"' WHERE `tm_id` = "+str(user_id)
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def setBinanceAPI(api, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `users` SET `binance_api`= '"+api.strip()+"' WHERE `tm_id` = "+str(user_id)
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def setPositionSize(position, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "REPLACE INTO `risk_settings` (`user_id`, `pos_size`) VALUES ("+str(user_id)+", "+str(position)+")"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def setSpreadPercent(spreat, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "REPLACE INTO `risk_settings` (`user_id`, `spread_per`) VALUES ("+str(user_id)+", "+str(spreat)+")"
	print(sql)
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def setTakeProfit(profit, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "REPLACE INTO `risk_settings` (`user_id`, `take_profit`) VALUES ("+str(user_id)+", "+str(profit)+")"
	#print(sql)	
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def setStopLoss(stoploss, user_id):
	connection = create_connection()	
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "REPLACE INTO `risk_settings` (`user_id`, `stop_loss`) VALUES ("+str(user_id)+", "+str(stoploss)+")"
	#print(sql)	
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()

def setTrigger(trigger, user_id):
	connection = create_connection()	
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "REPLACE INTO `trigger_hid` (`user_id`, `trigger_hid`) VALUES ("+str(trigger)+", "+str(user_id)+")"
	#print(sql)	
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()	

def getbinanceapi(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `binance_api` FROM `users` WHERE `tm_id` = "+str(user_id))
	api = cursor.fetchone()
	connection.close()
	if api:
		return api
	return None

def getbittrexapi(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `bittrex_api` FROM `users` WHERE `tm_id` = "+str(user_id))
	api = cursor.fetchone()
	connection.close()
	if api:
		return api
	return None