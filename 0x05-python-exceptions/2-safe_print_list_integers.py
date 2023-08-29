#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    index = 0
    
    while printed_integers < x:
        try:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end=" ")
                printed_integers += 1
        except IndexError:
            break 
        index += 1
    
    print()
    return printed_integers
