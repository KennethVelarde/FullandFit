import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def read_from_db(var):
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
	return menu

menu = read_from_db("JambaJuice")
print(menu[10])
c.close()
conn.close()

