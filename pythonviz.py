import sqlite3 as lite
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns


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

    
        
except lite.Error as e :
    
    print ("Error %s:" % e.args[0])
    sys.exit(1)

finally:
    
    if con:
        con.close()

#average of SO1 scores
#avgso1 = round(np.mean(SO1),2)
#print(avgso1)

#Combined SO1 and PEO1 Histogram
a = np.array(PEO1) 
b = np.array(SO1)
bins = (50,60,70,80,90,100)

sns.set()

plt.hist([a, b], bins, label=['PEO1', 'SO1'])
plt.title("Distribution of Scores for PEO1 and SO1")
plt.legend(loc='upper right')
plt.show()

#Combined interactive histograms with plotly, proof of concept, creates a plot
#online using an API and is stored at https://plot.ly/~bschenkman/0
#PEO1Hist = go.Histogram(
#    x=a,
#    opacity=0.75
#)
#SO1Hist = go.Histogram(
#    x=b,
#    opacity=0.75
#)

#data = [PEO1Hist, SO1Hist]
#layout = go.Layout(barmode='overlay')
#fig = go.Figure(data=data, layout=layout)

#py.iplot(fig, filename='overlaid histogram')