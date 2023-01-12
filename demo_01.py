# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:41:34 2022

@author: vto747

    Demonstrate the basic logic structures AND some basic Python BUILT-IN
    FUNCTIONS.
    
    Accept input from user & display input, character by character, in 
    various manners.
"""
# Use the BUILT-IN FUNCTION 'input' to prompt for input & accept & store it
txtInput = input( "Enter a string of text:  " )

# Use the BUILT-IN FUNCTION 'len' to retrieve the LENGTH of the input
txtLength = len( txtInput )

# Use the BUILT-IN FUNCTION 'print' to "mirror" input to user 
print( "\nYou entered: ", txtInput )
# Inform the user of the length of the input - demonstrates use of 'print'
print( "The string you entered is", txtLength, "characters long.\n" )


# Use a SELECTION structure to test the length of the input string
if ( txtLength == 10 ):
    print( "BINGO! You are today's winner." )
else:
    print( "Your string is", txtLength, "long." )
# end of SELECTION structure

# Print a 'header' line to separate output
print( "\n\n\nEach character, one per line:" )

# Use the BUILT-IN FUNCTION 'range' to print every character, one per line
for item in range( txtLength ):
    print( txtInput[ item ] )
    item = item + 10               # This really has no effect...
# end ITERATION structure

# Print EVERY OTHER character, using a different form of 'range'
print( "\n\nNow EVERY OTHER character..." )
for item in range( 0, txtLength, +2 ):
    print( txtInput[ item ] )
# end ITERATION structure


# Use the 'range' FUNCTION to print each character, one per line, in REVERSE
print( "\n\nNow all characters in REVERSE ORDER..." )
for item in range( txtLength-1 , -1, -1 ):
    print( txtInput[ item ] )
# end ITERATION structure


# Just 'cause :-) 
print( "\n\nThat's all folks!" )
















