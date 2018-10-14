import sqlite3 as lite
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

#clear connection variable
con = None

#connect to db and return sample data
try:
    con = lite.connect('sampledb.sqlite')
    
    cur = con.cursor()    
    #cur.execute('SELECT SQLITE_VERSION()')

    #data = cur.fetchone()
    
    #print ("SQLite version: %s" % data)

    #PEO1 Scores
    cur.execute('SELECT Score from Assignments where PEO = "PEO1"')
    PEO1 = cur.fetchall()

    #SO1 Scores
    cur.execute('SELECT Score from Assignments where SO = "SO1"')
    SO1 = cur.fetchall()

    avgso1 = np.mean(SO1)

    #for row in rows:
    #print (rows)
        
except lite.Error as e :
    
    print ("Error %s:" % e.args[0])
    sys.exit(1)

finally:
    
    if con:
        con.close()

print(avgso1)

a = np.array(PEO1) 
plt.hist(a) 
plt.title("Distribution of Scores for PEO1")
plt.show()