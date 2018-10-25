# TDD++

## Introduction

This project seeks to further expand on some basic principles of test-driven-development in Python, and to prove out the team's ability to code solutions in Python independent of the original TDD project. 

We chose to relate this to our Mendix project in that we are using a mocked up "sample data" database that would theoretically be available via our application.

## Code Samples

Sample of visualization code

>#Combined SO1 and PEO1 Histogram

>a = np.array(PEO1) 

>b = np.array(SO1)

>bins = (50,60,70,80,90,100)

>#setting style to seaborn to make it look better: https://seaborn.pydata.org/tutorial/aesthetics.html

>sns.set()

>plt.hist([a, b], bins, label=['PEO1', 'SO1'])

>plt.title("Distribution of Scores for PEO1 and SO1")

>plt.legend(loc='upper right')

>plt.show()

## Installation

Required libraries:

>matplotlib

>numpy

>plotly

>seaborn

>bokeh