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
		item["egg"] = column[6]
		item["milk"] = column[7]
		item["peanut"] = column[8]
		item["shellfish"] = column[9]
		item["soy"] = column[10]
		item["treenuts"] = column[11]
		item["wheat"] = column[12]
		menu.append(item)
		id+=1
	c.close()
	conn.close()
	return menu


menu = read_from_db("JambaJuice")
