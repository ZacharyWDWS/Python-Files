#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:07:52 2022

@author: zachwhittenton
"""
import pandas as pd
origFrame = pd.read_csv( 'ISCS_Scheds_5YR.csv' ) 
print(origFrame.shape)
"""
    Lets grab and store the column names from the DataFrame. We will use
    teh resulting INDEX object later to locate the columns we want...
"""
colNames = origFrame.columns
print("Count of columns in DataFrame: ",len(colNames))
print(colNames, "\n\n")
"""
    We will be using the 'slice'VIEW several times. its not very
    efficient to keep 'slicing' the exact same data, over & over.
    Yet, we really do not need to copy the slice and create a NEW,
    DISCREATE DataFrame object.
    Instead, we will give a NAME to the VIEW so that it can be retained 
    and re-used at need.
"""
colList =['Semester', 'Course', 'Section', 'Seats']
seatsView = origFrame.loc[:,colList]   #thsi is the view
print("Our new structure is a a(n)", type(seatsView))
print("Shape of  seatsView is", seatsView.shape)
"""
    My usual STARTING POINT for any analysis is to gather descriptive 
    statistics, t oget a feel for hte data...

    AGGREGATE data in the VIEW... 
"""
#finding the MEAN
print("Mean of Seats: %.4f"% #4 decimals
      seatsView['Seats'].mean())
#Finding the MEDIAN
print("Median of Seats: %d"% #no decimals
      seatsView['Seats'].median())
#Finding the MODE
print("mode of Seats: %d"%
      seatsView['Seats'].mode())
#Finding the Minimum
print("Minimum of Seats: %d"%
      seatsView['Seats'].min())
#Finding the MAXIMUM
print("Maximum of Seats: %d"%
      seatsView['Seats'].max())
#Finding the STANDARD DEVIATION
print("Standard Deviation of Seats: %.4f"%
      seatsView['Seats'].std())
#Finding the VARIANCE
print("Variance of Seats: %.4f"%
      seatsView['Seats'].var())
"""
    It might be even more useful to GROUP DATA before doing hte basic
    STATS calculations.
"""
with pd.option_context( 'display.max_rows', None):
    print( seatsView.groupby('Course')['Seats'].mean())
    """
        seatsView is our viw for our analysis, the groupby funcion
        is to group data by a column value, and we pick the colum nwe 
        want to group on, then we pick the column to calculate, lastly
        the mean is the aggregation
    """
#end context
byCourse =origFrame.groupby('Course') #View
courseAggs = byCourse.agg({'Seats': 'sum',
                           'Enrolled': 'sum'})
with pd.option_context( 'display.max_rows', None):
    print(courseAggs)
#end context












