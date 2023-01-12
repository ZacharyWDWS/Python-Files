#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:15:32 2022

@author: zachwhittenton
"""

"""
    We will "Clean up" some of the data in the DataFrame - this
    is the TRANSFORM step in the ETL proccess
"""

import pandas as pd

# Declare a DataFame object and "load" it with the schedule data
initialFrame = pd.read_csv( 'ISCS_Scheds_5YR_orig.CSV' )
print( "Checking.. the Shaoe of the DataFrame is: ", initialFrame.shape)

print(initialFrame.head())

"""
    Let's replace the 'nan' in the notes with something that CLEARLY indicates 
    taht there are NO NOTES for that section... ("NONE")
"""
# This edits the ORIGINAL CSV
initialFrame[ 'Notes' ] = initialFrame[ 'Notes' ].fillna('NONE')
print(initialFrame.head())

initialFrame[ 'Wait List' ] = initialFrame[ 'Wait List' ].fillna(0)

"""
    After our TRANSFORMS, we want to save the DATAFRAME OBJECT, as a
    COMPLETE, COHESIVE UNIT - that way we can bring it back DIRECTLY 
    as a DataFrame Object.
"""
initialFrame.to_pickle('cleanFrame.pkl')

