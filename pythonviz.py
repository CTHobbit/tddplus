import sqlite3 as lite
import sys

#clear connection variable
con = None

#connect to db and return sample data
try:
    con = lite.connect('sampledb.sqlite')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()
    
    print ("SQLite version: %s" % data)

    cur.execute('SELECT * from Assignments')

    rows = cur.fetchall()

    for row in rows:
        print (rows)
        
except lite.Error as e :
    
    print ("Error %s:" % e.args[0])
    sys.exit(1)
    
finally:
    
    if con:
        con.close()