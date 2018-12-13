import pymysql
import re
import json
from connection import create_connection, save

def addbroadcastmsg(user_id, message):

	data = {
		"tm_id": user_id,
		"message": message
	}

	save('broadcasting_msg', data)

def get_users_by_channel_id(channel_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `user_id` FROM `using_channels` WHERE `is_enable` = 1 AND `channel_id` = "+str(channel_id))

	users = []
	for ch in cursor.fetchall():
		users.append(ch)
	connection.close()

	return users


def getusers_forbroadcastmessage():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `tm_id` FROM `users` WHERE `is_enable` = 1")

	users = []
	for ch in cursor.fetchall():
		users.append(ch)
	connection.close()

	return users


def getchannelbyid(channel_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `channel_name`, `oldchannel_name` FROM `channels` WHERE `id` = "+str(channel_id))
	ch = cursor.fetchone()	
	connection.close()
	return ch


def get_binancechannels_admin():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `id`,`channel_name`, `is_enable` FROM `channels` WHERE `is_bittrex` = 0")

	channels = []
	for ch in cursor.fetchall():
		channels.append(ch)
	connection.close()

	return channels


def get_bittrexchannels_admin():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `id`,`channel_name`, `is_enable` FROM `channels` WHERE `is_bittrex` = 1")

	channels = []
	for ch in cursor.fetchall():
		channels.append(ch)
	connection.close()

	return channels


def createChannel(channel_name):
	data = {
		"channel_name": channel_name
	}

	save('channels', data)

def change_channelname(channel_id, newchannel_name):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `channel_name` FROM `channels` WHERE `id` = "+str(channel_id))
	ch = cursor.fetchone()
	sql = "UPDATE `channels` SET `channel_name`= '"+newchannel_name+"', `oldchannel_name` = '"+ch['channel_name']+"' WHERE `id` = "+str(channel_id)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	connection.close()


def getbinanceapi(user_id):
	connection = create_connection()	
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `binance_api` FROM `admins` WHERE `tm_id` = "+str(user_id))
	api = cursor.fetchone()

	connection.close()
	if api:
		return api
	return None


def getbittrexapi(user_id):
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `bittrex_api` FROM `admins` WHERE `tm_id` = "+str(user_id))
	api = cursor.fetchone()
	
	connection.close()
	if api:
		return api
	return None


def getTotalUsers():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT count(*) as count FROM `users`")
	count = cursor.fetchone()
	
	connection.close()
	if count:
		return count['count']
	return False


def getActiveUsers():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT count(*) as count FROM `users` TIME_TO_SEC(TIMEDIFF(NOW(), `last_active`))/3600 < 5")
	count = cursor.fetchone()
	
	connection.close()
	if count:
		return count['count']
	return False


def getDisableUsers():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT count(*) as count FROM `users` TIME_TO_SEC(TIMEDIFF(NOW(), `last_active`))/3600 > 5 AND `is_enable` = 1")
	count = cursor.fetchone()
	
	connection.close()
	if count:
		return count['count']
	return False


def getDefaultMsg():
	connection = create_connection()	
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `default_message` FROM `messages`")
	msg = cursor.fetchone()
	
	connection.close()
	if msg:
		return count['default_message']
	return False


def getCustomMsg():
	connection = create_connection()
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	cursor.execute("SELECT `custom_message` FROM `messages`")
	msg = cursor.fetchone()
	
	connection.close()
	if msg:
		return count['custom_message']
	return False


def setCustomMsg(msg):
	connection = create_connection()	
	cursor = connection.cursor(pymysql.cursors.DictCursor)
	sql = "UPDATE `messages` SET `custom_message`='"+str(msg)+"'"
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
	connection.close()