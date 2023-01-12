#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:16:35 2022

@author: zachwhittenton
"""

"""
    We will use Pandas to SLICE ROWs from the DataFram
"""
import pandas as pd
dataFrame = pd.read_csv( 'ISCS_Scheds_5YR.csv' ) 

print(type(dataFrame))
print(dataFrame)
print(dataFrame.shape)
"""
    Maybe we want to KEEP the SHAPE data for later use...
    
    We will give a name to the TUPLE so that we can use it later
"""
orig_stats = dataFrame.shape
"""
    We will now UNPACK the TUPLE into individual variables,
    using MULTIPLE ASSIGNMENT
"""
rowCount, colCount = orig_stats
"""
    We can SLICE a SINGLE ROW from the DataFrame...
"""
print(dataFrame.loc[17])
"""
    we can SLICE out CONTIGUOUS GROUOS if ROWS...
    ...This will be a NON_PERSISTENT VIEW
"""
print( dataFrame.loc[823:828])
"""
    OR, we can create a PERSISTENT VIEW into the ORIGINAL
    DataFrame
"""
slicedRows = dataFrame.loc[823: 828]
print(type(slicedRows))
print(slicedRows)
print(slicedRows.shape)
"""
    if we will me MANIPULATING DATA, we really want to create a SECOND,
    SEPARATE, DISCRETE DataFrame containing ONLY our desired SLICE
"""
cbkFrame = pd.DataFrame( dataFrame.loc[ 539: 543 ] )
print(type(cbkFrame))
print(cbkFrame)
print(cbkFrame.shape)










