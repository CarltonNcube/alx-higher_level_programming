#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

# If the last digit is greater than 5: print "is greater than 5"
if last_digit > 5:
    print("Last digit of", number, "is greater than 5")
# If the last digit is 0: print "is 0"
elif last_digit == 0:
    print("Last digit of", number, "is 0")
# If the last digit is less than 6 and not 0: print "is less than 6 and not 0"
else:
    print("Last digit of", number, "is less than 6 and not 0")
