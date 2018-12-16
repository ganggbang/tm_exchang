import pymysql


def create_connection():
	return pymysql.connect(
		host='104.248.72.209',
		user='tm_user2',
		password='evn3n8FD1JL33eha',
		db='tm'
	)


def save(table, data):
	connection = create_connection()

	# new_data = {}
	#
	# for key, value in data.items():
	# 	new_data[key] = str(value)
	#
	# print(new_data)

	sql = "INSERT IGNORE INTO %s SET %s" % (
		table,
		", ".join(
			"`%s`='%s'" % (field, value.replace("None", "").replace("'", "''").replace("\n", " ")) for field, value in data.items()))
	# print(sql)
	#  return None
	cursor = connection.cursor()
	cursor.execute(sql)
	last_id = cursor.lastrowid
	connection.commit()
	cursor.close()
	connection.close()
	return last_id
