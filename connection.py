import pymysql

def create_connection():
	return pymysql.connect(
		host='localhost',
		user='tm_user',
		password='3mer9cuc0vIlrfOv',
		db='tm'
	)

def save(connection: pymysql.connections.Connection, table, data):
	new_data = {}

	for key, value in data.items():
		new_data[key] = str(value)

	print(new_data)

	sql = "INSERT IGNORE INTO %s SET %s" % (
		table,
		", ".join(
			"`%s`='%s'" % (field, value.replace("None", "").replace("'", "''").replace("\n", " ")) for field, value in new_data.items()))
	# print(sql)
	#  return None
	cursor = connection.cursor()
	cursor.execute(sql)
	last_id = cursor.lastrowid
	connection.commit()
	cursor.close()
	return last_id
