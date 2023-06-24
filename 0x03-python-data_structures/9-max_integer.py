#!/usr/bin/python3

integer(my_list=[]):
    if my_list = 0:  # Check if the list is empty
        return None
    
    max_num = my_list[0]  # Assume the first element is the maximum
    
    for num in my_list:
        if num > max_num:  # Update the maximum if a larger number is found
            max_num = num
    
    return max_num
