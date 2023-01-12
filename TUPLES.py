#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with a tuple data structure

@author: zachwhittenton
"""

# IMUTABLE = it cannot be changed.
# TUPLES have natural security.
# in a oredefined order which makes us have an index relationship with tuples.

# TUPLES are only defined by "()".
courses = ( "IS1003", "IS1403", "IS3003", "IS053", "IS2063" ) 

#returns the type of courses
print( " The TYPE of the variable courses is", type(courses) )
#returns the length of courses
print( "the LENGTH of the variable courses is", len(courses) )

#version 1
# we can iterate through our TUPLE using the index values
print(" \n\nIterating through the TUPLE via INDEX" )
for indexNum in range( len(courses)):
    print( "\n", courses[indexNum])
# end iteration

#version 2
# A SIMPLER approach
print ( "\n\n\nAnother iteration approach" )
for element in courses:
    print("\n", element)
# end iteration

# we can also find specifi values in our TUPLE 
findThis = input( "Which course are you looking for?    ")
print("Your course is Located at index ", courses.index(findThis))


# TUPLES can contain duplicate ELEMENTS. We can check that
print("\n\n There are", courses.count("IS1403"),
      "instances of IS1403 in courses.")











