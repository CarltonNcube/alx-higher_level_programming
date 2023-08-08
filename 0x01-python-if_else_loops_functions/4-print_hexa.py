#!/usr/bin/python3
#for loop that will iterate over the numbers 0 to 98 (99 numbers in total)
#i will take on each of these values in sequence.
#it uses string format is used to define the desired output format
for i in range(0, 99):
    print("{} = 0x{:02x}".format(i, i))
