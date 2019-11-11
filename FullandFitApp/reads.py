import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM JambaJuice')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)


read_from_db()

c.close()
conn.close()

