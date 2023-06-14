#!/usr/bin/python3

def print_list_integer(my_list=[]):
    my_list = list(range(1, 6))
    for number in my_list:
        print("{:d}".format(number))
print_list_integer(my_list)
