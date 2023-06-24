#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:

        return None
# Assume the first element is the maximum    
    max_num = my_list[0]
    
    for num in my_list:
# Update the maximum if a larger number is found
        if num > max_num:
            max_num = num
    
    return max_num
