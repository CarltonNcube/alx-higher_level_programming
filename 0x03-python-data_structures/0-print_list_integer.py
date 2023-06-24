#!/usr/bin/python3

# Create a list containing the numbers 1 to 5
# Call the function with the numbers list

def print_list_integer(my_list=[]):
    for number in my_list:
        print("{:d}".format(number))

numbers = [1, 2, 3, 4, 5]
print_list_integer(numbers)
