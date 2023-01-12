# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:16:41 2022

@author: Zachary
"""
myInput = input("Please enter a multi-word phrase and press Enter: ")
length = len(myInput)

while length < 10:
    
    print("You entered: " + myInput)
    print("The length of your phrase is " + str(length))
    print("You must enter a new phrase, at least 10 characters long. ")
    myInput = input("Please enter a multi-word phrase and press Enter: ")
    length = len(myInput)
       
print("You entered: " + myInput)
print("The length of your phrase is " + str(length))
print("Individual Characters in you phrase: ")
 
for number in range(len(myInput)):
    print(myInput[number])