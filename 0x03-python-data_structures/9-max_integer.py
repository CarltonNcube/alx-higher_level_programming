#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list = []:  # Check if the list is empty

        return None
    
    max_num = my_list[0]  # Assume the first element is the maximum
    
    for num in my_list:
        if num > max_num:  # Update the maximum if a larger number is found
            max_num = num
    
    return max_num
