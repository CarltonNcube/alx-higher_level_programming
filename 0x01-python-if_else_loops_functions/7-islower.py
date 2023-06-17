#!/usr/bin/python3
#Returns True if c is lowercase
#Returns False otherwise

def islower(c):
    if c.islower():
        print(c, "is lowercase")
        return True
    elif c.isupper():
        print(c, "is uppercase")
        return False
    else:
        print("_")
