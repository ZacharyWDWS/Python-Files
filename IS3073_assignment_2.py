# -*- coding: utf-8 -*-
"""
Assignment 02 

 "Slicing" a NumPy Array
 
 
 There are five (5) tasks to be completed in this assignment.
     01   Make the NumPy library available in your script.
     02   Use the provided data to create/instantiate/load a NumPy Array
          object. You may name this object as you wish (NO SINGLE CHARACTERS!).
     03   "Slice" out and display the specified (complete) ROW of data.
     04   "Slice" out and display the specified (complete) COLUMN of data.
     05   "Slice" out and display the specified CELL (ROW x COLUMN) of data.

 Refer to the instructions for details.
 
"""

"""
    The data to be loaded into the NumPy array is provided below as a 
    two-dimentional "raw" array - a List of List objects.
    
    Use this data, AS PRESENTED HERE, to build/instantiate your NumPy Array.
"""


#======================  ADD YOUR CODE BELOW THIS COMMENT ====================
# Task 01 importing numpy
import numpy as np

# Task 02 assigning my data to the numpy array
assignData = np.array([ [ "0214", 75.52048,	 36.28048,  57.46348  ],
               [ "0215", 78.92248,	 45.22648,  62.13748  ],
               [ "0216", 81.424484, 48.98848,  64.35823  ],
               [ "0217", 82.30648,  45.46048,  63.89548  ],
               [ "0218", 82.97248,  43.588478, 62.023483 ],
               [ "0219", 83.99848,  42.05848,  59.906235 ],
               [ "0220", 82.73848,  41.914482, 61.406235 ],
               [ "0221", 84.73648,  51.77848,  67.45423  ],
               [ "0222", 85.60048,  51.940483, 67.01323  ],
               [ "0223", 88.76848,  53.93848,  68.73974  ],
               [ "0224", 85.97848,  50.338478, 66.93598  ],
               [ "0225", 83.99848,  50.87848,  65.30323  ],
               [ "0226", 84.30448,  46.99048,  65.03773  ],
               [ "0227", 86.284485, 49.56448,  65.61672  ],
               [ "0228", 83.02648,  36.55048,  56.65498  ]
             ])
# prints our np array
print( "This is our array called assignData\n" )
print(assignData)

# Task 03 slice the 8th row 
print( "\n\nThis is the 8th row from the array\n",
      assignData[8])

# task 04 slice the 3rd column
print(" \n\nThis is the 3rd column from the array\n ",
      assignData[:,2])

# task 05 slice out a single sell from the 2nd column and 9th row of the array
print(" \n\nThis is slicing a single cell from the array\n ",
      assignData[9,2])







