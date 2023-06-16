#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# if number is greater than 0, print "is positive"
if number > 0:
    print(number, "is positive")
# if number is 0, print "is zero"
elif number == 0:
    print(number, "is zero")
# else if number is negative, print "is negative"
else:
    print(number, "is negative")
