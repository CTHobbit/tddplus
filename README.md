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

>pandas

>plotly

>seaborn

>bokeh

## Notes on where we ended up. 

Moved further through testing although we ran into several issues related to our database items having multiple fields that were getting us stuck. This was simplified in order to get an initial migration done. 

In the original TDD assignments each item in the data base was a single text field. Our data for the assigment data was made up of multiple fields per row. This proved to be problimatic when trying to adapt from the original assigment. 

We were able to add a button to the home page to call the viualization program. We are very close to having the button auto click in functional_tests but have been unable to have it recoginize the click method. 

