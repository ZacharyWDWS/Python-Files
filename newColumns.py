#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:51:04 2022

@author: zachwhittenton
"""

"""
    We will "Clean up" some of the data in the DataFrame - this
    is the TRANSFORM step in the ETL proccess
"""

import pandas as pd

# Declare a DataFame object and "load" it with the schedule data
newFrame = pd.read_pickle( 'cleanFrame.pkl' )
print( "Checking.. the Shaoe of the DataFrame is: ", newFrame.shape)

print(newFrame.head())

"""
    WE ened a UTILIZATION RATE for EACH ROW, but we don't have that...
    
    We can ADD a COLUMN to the DataFrame to hold that data FOR EACH
    INDIVIDUAL ROW IN THE DATAFRAME.
"""
"""
creates a new column UTILIZATION that has the valeus of
the enrolled colum divided by the seats column
"""
newFrame["Utilization"] =                                \
       ( newFrame['Enrolled'] / newFrame['Seats'])
print(newFrame.head())

"""
    Now that we have ADDED a new column, we want to PICKLE
    the DataFrame again, with the NEW COLUMN included...
"""
newFrame.to_pickle('forAnalysis.pkl')
