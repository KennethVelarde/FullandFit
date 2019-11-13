import sqlite3

def get_menu(var): 
	string_var = str(var)
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	c.execute('SELECT * FROM FullMenu WHERE id = ' + string_var) 
	menu = []
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
	c.close()
	conn.close()
	return menu

def get_restaurants(): 	
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	restaurant = []
	c.execute('SELECT * FROM restaurants')
	for row in c.fetchall():
		item = []
		item.append(row[0]) 
		item.append(row[1])
		item.append(row[2])
		restaurant.append(item)
	c.close()
	conn.close()
	return restaurant

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

