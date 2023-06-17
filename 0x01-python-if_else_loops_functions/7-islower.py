#!/usr/bin/python3
#This code uses ord() function to get the ASCII value of the character.
#Lowercase letters in ASCII range from 97 to 122
#while uppercase letters range from 65 to 90
#By comparing the ASCII value of the character c with these ranges, you can determine if it is lowercase or uppercase.

def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        print(c, "is lowercase")
        return True
    elif ord('A') <= ord(c) <= ord('Z'):
        print(c, "is uppercase")
        return False
    else:
        print("_")