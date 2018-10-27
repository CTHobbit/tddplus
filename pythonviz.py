import sqlite3 as lite
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row

#clear connection variable
con = None

#connect to db and return sample data
try:
    con = lite.connect('sampledb.sqlite')
    
    cur = con.cursor()    
    
    #PEO1 Scores
    cur.execute('SELECT Score from Assignments where PEO = "PEO1"')
    PEO1 = cur.fetchall()

    #SO1 Scores
    cur.execute('SELECT Score from Assignments where SO = "SO1"')
    SO1 = cur.fetchall()

    #PEO1 Scores by Year
    cur.execute('Select Year, Score from Assignments where PEO = "PEO1"')
    PEO1Scores = np.array(cur.fetchall())
    
        
except lite.Error as e :
    
    print ("Error %s:" % e.args[0])
    sys.exit(1)

finally:
    
    if con:
        con.close()


#Data for combined SO1 and PEO1 Histogram
a = np.array(PEO1) 
b = np.array(SO1)
bins = (50,60,70,80,90,100)

#Data for bar graph showing PEO1 by Year
PEO1Scores = PEO1Scores[PEO1Scores[:,0].argsort()]
x = PEO1Scores[:,0]
y = PEO1Scores[:,1]

#Creating a pandas dataframe for aggregation

data = np.int_(PEO1Scores)

dataset = pd.DataFrame({'Year': data[:,0],
                   'Score': data[:,1]})

#group data by year and average the scores for that year
datasetmean = dataset.groupby('Year', as_index=False)['Score'].mean()

#setting style to seaborn to make it look better: https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()

#Figures to display on-screen prior to html export

plt.figure(1)
plt.subplot(311)
plt.hist([a, b], bins, label=['PEO1', 'SO1'])
plt.title("Distribution of Scores for PEO1 and SO1")
plt.legend(loc='upper right')

#Scatter plot of scores by year
plt.subplot(312)
plt.ylabel('Scores')
plt.title('Individual Scores by Year')
plt.scatter(x,y)

#Bar chart of average score per year
plt.subplot(313)
plt.ylabel('Average Score')
plt.title('Average Scores by Year')
df = dataset.groupby(['Year'])['Score'].mean()
df.plot.bar()

plt.show()

p = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
p.circle(x,y, size=5, color="navy", alpha=0.5)

# Plot quad/histogram
hist_a, edges = np.histogram(a, density=True, bins=5)
hist_b, edges = np.histogram(b, density=True, bins=5)
p1 = figure(plot_width=400, plot_height=400)
p1.quad(top=hist_a, bottom=0, left=edges[:-1], right=edges[1:], alpha=0.4)
p2 = figure(plot_width=400, plot_height=400)
p2.quad(top=hist_b, bottom=0, left=edges[:-1], right=edges[1:], alpha=0.4)

# show the results
show(row(p, p1, p2))

# output to HTML file
output_file("accredplots.html")


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