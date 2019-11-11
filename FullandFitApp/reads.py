import sqlite3

def read_from_db(var):
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	menu = []
	c.execute('SELECT * FROM ' + var)
	for column in c.fetchall():
		item = {}
		id = 0
		item["name"] = column[0]
		item["price"] = column[1]
		item["calories"] = column[2]
		item["carbs"] = column[3]
		item["protein"] = column[4]
		item["fat"] = column[5]
		menu.append(item)
		id+=1
	c.close()
	conn.close()

	return menu

