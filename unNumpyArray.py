# -*- coding: utf-8 -*-
"""
This is the "longhand" version of using NumPy Array functionality
to calculate the square of every element in an array.

"""
# Declare an array ("little a") as a List of List objects
anArray = [ [ 0.0, 0.1, 0.2, 0.3 ], 
            [ 1.0, 1.1, 1.2, 1.3 ],
            [ 2.0, 2.1, 2.2, 2.3 ]  ] 

print( "Original array values " )
print( anArray )

"""
    Use a two-level (for two dimensions) nested loop to calculate the
    squares and to store the results into a new array ("little a")
    
    (This is something that NumPy can do for us - we'll look at that later.)        
"""
squared = []                        # Declare the List to hold the new array
for row in anArray:                 # Process each ROW of the array
    rowList = []                    # Declare a List to hold results / row
    for element in row:             # Process each element / column in ROW
        square = element**2
        rowList.append( square )    # Insert results into ROW level List
    # end element within row 
    squared.append( rowList )       # Insert ROW level List into array
# end row within array

print( "New array with squared values " )
print( squared )
