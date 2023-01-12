#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:17:39 2022

@author: zachwhittenton
"""

import pandas as pd
"""
    We will use the dataset ISCS_Scheds_5YR.csv
    for our demonstration
"""

myFirstDataFrame = pd.read_csv( 'ISCS_Scheds_5YR.csv' ) 

print( type( myFirstDataFrame ) ,"\n")
print(myFirstDataFrame)
print( myFirstDataFrame.shape ) 
"""
    Just as with our numpy array, we can "ask" the
    DataFrame objeect for its COLUMNS attribute
"""

print( myFirstDataFrame.columns )