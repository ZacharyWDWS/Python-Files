#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with a SET data structure

@author: zachwhittenton
"""

# little more complex than a TUPLE
# are not in a specific order, No guaranteed order
# cannot have duplicates
# Cant access via INDEX
# IMMUTABLE = cannot be changed

# Our SET starts with brackets {}
grades = { "A+", "A", "A-",
          "B+", "B", "B-",
          "C+", "C", "C-",
          "D+", "D", "D-",}

#returns the type of courses
print( " The TYPE of the variable grades is", type(grades) )
#returns the length of courses
print( "the LENGTH of the variable grades is", len(grades) )



# we can ADD elements to our SET
grades.add("F")

# We can iterate through our SET
print("\n\n Iterate through SET")
for element in grades:
    print(element)
    # end iteration
    

# we can REMOVE elements to or SET
grades.remove("F")

# We can iterate through our SET
print("\n\n Iterate through SET")
for element in grades:
    print(element)
    # end iteration
