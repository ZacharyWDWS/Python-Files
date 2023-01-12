#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:46:34 2022

@author: zachwhittenton
"""

import pandas as pd

"""
    We will use the dataset ISCS_Scheds_5YR.csv
    for our demonstration
"""

origFrame = pd.read_csv( 'ISCS_Scheds_5YR.csv' ) 

print(type(origFrame))
print(origFrame)
print(origFrame.shape)


"""
    "slicine" ROW 17 from the dATAFrame using ILOC
"""

print(origFrame.iloc[17])

#--------------------------------------------------------
"""
    Let's SLICE a GROUP of ROWS using both loc & iloc
"""
print( "Rows 3-5 using LOC")
print( origFrame.loc[3:5])

print( "Rows 3-5 using iLOC")
print( origFrame.iloc[3:6])

#-----------------------------------------------------------
"""
    one of hte ADVANTAGES to using iloc is that we can retrieve 
    NON-CONTIGUOUS ROWs of data.
    
    small steps...
"""
print( "Rows 3-5 using iLOC - NEW NOTATION STYLE")
print( origFrame.iloc[[3,4,5]])

#------------------------------------------------------------
"""
    If we want to REORDER the ROWs, we change the ORDER 
    in the list...
"""
print( "Rows 3-5 using iLOC - REORDERED")
print( origFrame.iloc[[5,4,3]])

"""
     Now let's get some NON-CONTIGUOUS ROWs...
"""
print( "\nNON-CONTIGUOUS Rows using iloc")
print( origFrame.iloc[[1,107,108,283,284,285]])

#------------------------------------------------------------------
"""
    Now we will look at a NEW CONCEPT that will elt us print
    entire DATAFRAMES or VIEWS
"""

myRows = origFrame.iloc[[1,107,108,283,284,285]]

print( "\nPRINT ALL DATA from VIEW")

with pd.option_context("max_rows", None,
                       "max_columns", None):
    print(myRows)
# end of LOGIC STRUCTURE / WITH / CONTEXT





    