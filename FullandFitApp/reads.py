import sqlite3

def read_from_db(var):
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	restaurant = []
	menu = []
	c.execute('SELECT * FROM restaurants WHERE rowid = ' + var)
	res_list = c.fetchall()[0] 
	id  = res_list[0]
	restaurant.append(id) 
	restaurant.append(res_list[1])
	restaurant.append(res_list[2])
	  
	id_string = str(id)
	c.execute('SELECT * FROM FullMenu WHERE id = ' + id_string) 
	for row in c.fetchall():
		item = {}
		item_id = 0
		item["id"] = item_id
		item["name"] = row[0]
		item["price"] = row[2]
		item["calories"] = row[3]
		item["carbs"] = row[4]
		item["protein"] = row[5]
		item["fat"] = row[6]
		item["egg"] = row[7]
		item["milk"] = row[8]
		item["peanut"] = row[9]
		item["shellfish"] = row[10]
		item["soy"] = row[11]
		item["treenuts"] = row[12]
		item["wheat"] = row[13]
		menu.append(item)
		item_id+=1
	restaurant.append(menu)
	c.close()
	conn.close()
	return restaurant

