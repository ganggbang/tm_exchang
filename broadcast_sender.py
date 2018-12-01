#!/usr/bin/python3
import pymysql
import re
import json
from user import * 
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, RegexHandler,
						  ConversationHandler)
############################### Bot ############################################


bot = telegram.Bot('692136526:AAGbRDOH2uO35F6Em843eQDVLpiW6MFcLmk')

def sendbroadcastmessages(bot, chat_id, message):
	bot.send_message(chat_id=chat_id, text=message)	

messages = getbroadcastmessages()

for msg in messages:
	try:
		sendbroadcastmessages(bot, msg['tm_id'], msg['message'])	
	except Exception as e:
		print(e)
	setbroadcastmessages_sended(msg['id'])
