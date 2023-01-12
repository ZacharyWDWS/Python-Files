# -*- coding: utf-8 -*-
"""
We will repeat EXACTLY what unNumPyArray did.

This time, though, we will use a NumPy array for processing....

Our Array object will hold numbers the same numbers:
    
           Col 0     Col 1      Col 2     Col 3
           ------    ------     -----    ------
    Row 0     0.0       0.1       0.2       0.3
    Row 1     1.0       1.1       1.2       1.3
    Row 2     2.0       2.1       2.2       2.3
    
"""
import numpy as np

#=========================   Initial Instantiation & Load of an Array

anArray = np.array( [ [ 0.0, 0.1, 0.2, 0.3 ], 
                      [ 1.0, 1.1, 1.2, 1.3 ],
                      [ 2.0, 2.1, 2.2, 2.3 ]  ] )

print( "Our initial Array object contents:" )
print( anArray )
print( "The 'shape' of our Array is: ", 
        anArray.shape, "\n" )

"""
    Use the built-in NumPy functionality to produce a NEW ARRAY containing
    the squared values of the ORIGINAL array.       
"""
# If we need to KEEP the RESULTS, we need to build a new Array based on them
squared = np.array( np.square( anArray ) )
print( "\n\nA new Array, results of squaring anArray: " )
print( squared )
print( "The 'shape' of our Array is: ", 
        squared.shape, "\n" )

