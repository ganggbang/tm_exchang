import pymysql
import re
import json
from connection import create_connection, save

def is_settings(chat_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `user_id` FROM `risk_settings` WHERE `user_id` = "+str(chat_id))
	settings = cursor.fetchone()
	connection.close()
	return settings


def del_order(orderId):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "DELETE FROM `orders` WHERE `orderId` = '"+str(orderId)+"'"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def cancel_order(orderId):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `orders` SET `isCanceled`=1,`last_active`=NOW() WHERE `orderId` = '"+str(orderId)+"'"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def get_order(channel_id, orderId):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `ticker`,`exchange`, `last_active`, `orderId`, `quantity` FROM `orders` WHERE `channel_id` ="+str(channel_id)+" AND `orderId` = '"+str(orderId)+"'")
	order = cursor.fetchone()
	connection.close()
	return order


def get_orders_by_filled(channel_id, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)

	if channel_id == 0:
		sql = "SELECT `ticker`,`exchange`, `last_active`, `orderId`, `quantity` FROM `orders` WHERE `tm_id` = "+str(user_id)+" AND `isFilled` = 1"
	else:
		sql = "SELECT `ticker`,`exchange`, `last_active`, `orderId`, `quantity` FROM `orders` WHERE `channel_id` =" + str(channel_id) + " AND `tm_id` = " + str(user_id) + " AND `isFilled` = 1"

	cursor.execute(sql)

	orders = []
	for t in cursor.fetchall():
		orders.append(t)
	connection.close()
	return orders


def get_orders(channel_id, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `ticker`,`exchange`, `last_active`, `orderId`, `quantity` FROM `orders` WHERE `channel_id` ="+str(channel_id)+" AND `tm_id` = "+str(user_id)+" AND `isCanceled` = 0 AND `isFilled` = 0")

	orders = []
	for t in cursor.fetchall():
		orders.append(t)
	connection.close()
	return orders


def insert_order(channel_id, user_id, ticker, exchange, orderId, quantity):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "INSERT INTO `orders`(`tm_id`, `channel_id`, `ticker`, `exchange`, `orderId`, `last_active`, `quantity`) VALUES ("+str(user_id)+", "+str(channel_id)+", '"+ticker+"', '"+exchange+"', '"+str(orderId)+"', "+str(quantity)+", NOW())"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def sell_order(orderId):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `orders` SET `isSell`=1, `isFilled`=0, `last_active`=NOW() WHERE `orderId` = '"+str(orderId)+"'"
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
	cursor.execute("SELECT `message`,`id`, `channel_id` FROM `broadcasting_msg` WHERE `is_sended` = 0")

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


def get_usingchannels_by_channels(channels, user_id):
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

def get_channel(channel_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)

	cursor.execute("SELECT `channel_name`, `ticker`, `is_enable`, `is_bittrex` FROM `channels` WHERE `id` = "+str(channel_id))

	channel = cursor.fetchone()
	connection.close()

	return channel


def get_channels():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	#cursor.execute("SELECT `channel_name`, `id`, `is_enable` FROM `using_channels` WHERE `user_id` = "+str(user_id))
	cursor.execute("SELECT `channel_name`, `id`, `is_enable` FROM `channels` WHERE `is_enable` = 1")

	channels = []
	for ch in cursor.fetchall():
		channels.append(ch)
	connection.close()

	return channels


def get_usingchannels_byuserid(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	#cursor.execute("SELECT `channel_name`, `id`, `is_enable` FROM `using_channels` WHERE `user_id` = "+str(user_id))
	cursor.execute("SELECT `channel_id` FROM `using_channels` WHERE `is_enable` = 1 AND `user_id` = "+str(user_id))

	channels = []
	for ch in cursor.fetchall():
		channels.append(ch)
	connection.close()

	return channels


def checkuser(update):
	if existing_user(user_id) is False:
		user_id = update['message']['chat']['id']
		user = {
			"tm_id": update['message']['chat']['id'],
			"first_name": update['message']['chat']['first_name'],
			"last_name": update['message']['chat']['last_name'],
			"username": update['message']['chat']['username']
		}


		save('users', user)
		set_position_size_per(3, user_id)
		set_spread_percent(3, user_id)
		set_take_profit(30, user_id)



def existing_user(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `tm_id` FROM `users` WHERE `tm_id` = "+str(user_id))
	user_id = cursor.fetchone()
	connection.close()

	if user_id:
		return True
	return False


def get_users():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `tm_id`, `bittrex_api`, `binance_api` FROM `users` WHERE `is_enable` = 1 AND `bittrex_api` is NOT NULL AND `binance_balance` is NOT NULL")

	users = []
	for u in cursor.fetchall():
		users.append(u)
	connection.close()

	return users


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


def setBittrexAPI(api, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	if existing_user(user_id):
		sql = "UPDATE `users` SET `bittrex_api` = '"+api.strip()+"' WHERE `tm_id` = "+str(user_id)
	else:
		sql = "INSERT INTO `users` (`bittrex_api`, `tm_id`) VALUES ('"+api.strip()+"', ",+str(user_id)+")"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def setBinanceAPI(api, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	if existing_user(user_id):
		sql = "UPDATE `users` SET `binance_api` = '"+api.strip()+"' WHERE `tm_id` = "+str(user_id)
	else:
		sql = "INSERT INTO `users` (`binance_api`, `tm_id`) VALUES('"+api.strip()+"', "+str(user_id)+")"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def set_position_size_per(position, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	if existing_user(user_id):
		sql = "UPDATE `risk_settings` SET `pos_size_per` = "+str(position)+" WHERE `user_id` = "+str(user_id)
	else:
		sql = "INSERT INTO `risk_settings` (`user_id`, `pos_size_per`) VALUES ("+str(user_id)+", "+str(position)+")"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def get_position_size(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `pos_size_amount`,`pos_size_per` FROM `risk_settings` WHERE `user_id` = "+str(user_id))
	data = cursor.fetchone()
	connection.close()

	return data


def set_spread_percent(spread, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	if existing_user(user_id):
		sql = "UPDATE `risk_settings` SET `spread_per` = "+str(spread)+" WHERE `user_id` = "+str(user_id)
	else:
		sql = "INSERT INTO `risk_settings` (`user_id`, `spread_per`) VALUES ("+str(user_id)+", "+str(spread)+")"
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def get_spread_percent(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `spread_per` FROM `risk_settings` WHERE `user_id` = "+str(user_id))
	data = cursor.fetchone()
	connection.close()

	return data['spread_per']


def set_take_profit(profit, user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	if existing_user(user_id):
		sql = "UPDATE `risk_settings` SET `take_profit` = "+str(profit)+" WHERE `user_id` = "+str(user_id)
	else:
		sql = "REPLACE INTO `risk_settings` (`user_id`, `take_profit`) VALUES ("+str(user_id)+", "+str(profit)+")"
	#print(sql)
	cursor.execute(sql)
	cursor = connection.cursor()
	connection.commit()
	cursor.close()
	connection.close()


def get_take_profit(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `take_profit` FROM `risk_settings` WHERE `user_id` = "+str(user_id))
	data = cursor.fetchone()
	connection.close()

	return float(data['take_profit'])


def get_howpercentage(part, whole):
	return 100 * float(part)/float(whole)


def get_percentage(percent, whole):
	return(percent * float(whole)) / 100.0


