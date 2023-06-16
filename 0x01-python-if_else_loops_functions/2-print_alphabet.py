#!/usr/bin/python3

#Print the lowercase letters from 'a' to 'z' 
alphabet = "" # create an empty string variable
for i in range(97, 123): # loop from 97 to 122, which are the ASCII codes for 'a' to 'z'
    alphabet = "{}{}".format(alphabet, chr(i)) # use the format() method to insert the character corresponding to the ASCII code into the string variable
print(alphabet)
