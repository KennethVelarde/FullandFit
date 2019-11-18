import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def destroy_table(): 
	c.execute('DROP TABLE IF EXISTS restaurants')
	
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS restaurants(id INTEGER, name TEXT, picture TEXT)')

def data_entry():
    c.execute("INSERT INTO restaurants VALUES ('1', 'Carls Jr.', '/FullandFit/FullandFitApp/static/img/thumbnails/CarlsJr.gif')")
    c.execute("INSERT INTO restaurants VALUES ('2', 'The Den', '/FullandFit/FullandFitApp/static/img/thumbnails/TheDen.png')")
    c.execute("INSERT INTO restaurants VALUES ('3', 'Taco Bell', '/FullandFit/FullandFitApp/static/img/thumbnails/TacoBell.jpeg')")
    c.execute("INSERT INTO restaurants VALUES ('4', 'Round Table', '/FullandFit/FullandFitApp/static/img/thumbnails/RoundTable.png')")
    c.execute("INSERT INTO restaurants VALUES ('5', 'Jamba Juice', '/FullandFit/FullandFitApp/static/img/thumbnails/jambajuice.png')")
    conn.commit()


def read_from_db():
    c.execute('SELECT * FROM restaurants')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)
#destroy_table()
create_table()
data_entry()
read_from_db()
c.close()
conn.close()



