#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# if number is greater than 0 and less than or equal to 10, print "is positive"
if number in range(1, 11):
    print("is positive")
# elif number is less than 0 and greater than or equal to -10, print "is negative"
elif number in range(-10, 0):
    print("is negative")
# else if number is 0, print "is zero"
elif number == 0:
    print("is zero")
else:
    print("Out of range")
