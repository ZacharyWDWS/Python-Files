#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:48:03 2022

@author: zachwhittenton
"""

import pandas as pd

"""
    We will use the dataset ISCS_Scheds_5YR.csv
    for our demonstration
"""

origFrame = pd.read_csv( 'ISCS_Scheds_5YR.csv' ) 

print(origFrame.shape)

rowCount, colCount = origFrame.shape
print("\nThere are %d rows, each with %d columns in the DataFrame." %
      (rowCount, colCount))

"""
    We need to SLICE out the COLUMNS we wish to run our preliminary
    analysis on...
    
        Semester, Course, Section, Seats
"""

colNames = origFrame.columns
print(colNames)

colList = ['Semester', 'Course', 'Section', 'Seats']

avaliable = origFrame.iloc[ :, ]