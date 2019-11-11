import sqlite3

conn = sqlite3.connect('db.sqlite3')
res = conn.execute("")
c = conn.cursor()

def read_from_db(var):
    c.execute('SELECT * FROM ' + var)
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)


read_from_db()
#changes
c.close()
conn.close()

