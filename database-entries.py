import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS restaurants(id REAL, name TEXT, picture TEXT)')

def data_entry():
    c.execute("INSERT INTO restaurants VALUES ('03', 'Taco Bell', '/FullandFit/FullandFitApp/static/img/thumbnails/TacoBell.jpeg')")
    c.execute("INSERT INTO restaurants VALUES ('04', 'Round Table', '/FullandFit/FullandFitApp/static/img/thumbnails/RoundTable.png')")
    c.execute("INSERT INTO restaurants VALUES ('05', 'Jamba Juice', '/FullandFit/FullandFitApp/static/img/thumbnails/jambajuice.png')")
    conn.commit()


def read_from_db():
    c.execute('SELECT * FROM restaurants')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

#create_table()
#data_entry()
read_from_db()
c.close()
conn.close()



