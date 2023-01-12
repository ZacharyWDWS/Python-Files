#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:53:23 2022

@author: zachwhittenton
"""

"""
 It's often EASIER (and more logical) to establish a ROW INDEX the
 we (the programmer) choose. Ideally, the row index/label shoudl be UNIQUE
 for each ROW in the dataset/DataFrame.

 Our challenge is that there is no single COLUMN whose value will
 UNIQUELY IDENTIFY each individual ROW in our data.

 However, Pandas will allow us to use a COMBINATION of COLUMNS to create
 what is known as a MULTILEVEL INDEX or MULTIINDEX.

 A MultiIndex is a HIERARCHICAL INDEX. These can be EXTREMELY USEFUL in
 many analysis & reporting situations.

 For our data, a combination of 'Semester' and 'CRN' will create a
 UNIQUE KEY or INDEX LABEL for each of our rows.


 """
import pandas as pd

initialFrame = pd.read_csv( 'ISCS_Scheds_5YR_orig.CSV',
index_col = [ 'Semester', 'CRN' ] )

"""
 Let's print a "chunk" of the newly MUTIINDEXED VIEW to see what this
 looks like.
"""
with pd.option_context( 'max_rows', None,
                     'max_columns', None ):
    print( "\n Using the MultiIndex" )
    print( initialFrame[ [ 'Course', 'Section', 'Title' ] ].head( 200 ) )
    # END CONTEXT