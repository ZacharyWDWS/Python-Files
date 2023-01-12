#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with LIST STRUCTURES

@author: zachwhittenton
"""

# They are orederd which means we can index
# we can change elements at a certain index
# mutable = changebale
# lists will allow duplicate elements

courses = [ "IS1003", "IS3003", "IS2063", "IS1403", "IS2053" ]

#returns the type of courses
print( " The TYPE of the variable courses is", type(courses) )
#returns the length of courses
print( "the LENGTH of the variable courses is", len(courses) )

# Print using INDEX
print("The ELEMENT at INDEX 2 is",
      courses[2])

# we can change the ELEMENT in the LIST using the index
courses[3] = "IS1413"

# add elements
# append adds to the end of the list
courses.append("IS1403")
courses.append("IS3003")

# pop will take the last element out if there is nothing in its function
courses.pop()
courses.pop(0)

# sometimes we need to REORDER the LIST
courses.sort()
print("The LISTS SORTED in ASCENDING ORDER")
for each in courses:
    print(each)