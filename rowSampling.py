#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:16:38 2022

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
    We will create a LIST containing ROW LABELS that has been
    quasi-randomized.
        
    We use the RANGE FUNCTION to do this...
"""

sample = range( 37, rowCount, 29 )

"""
    SLICE OUT the rows with labels matching our list elements
"""
trainingSet = origFrame.iloc[ sample ]

print(trainingSet)
print("here\n\n\n\n")
with pd.option_context( 'max_rows',    None,
                        'max_columns', None):
    print(trainingSet)
#end CONTEXT SCOPE