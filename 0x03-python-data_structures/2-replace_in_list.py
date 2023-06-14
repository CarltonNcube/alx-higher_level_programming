#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return list(my_list)
    my_list[idx] = element
    return my_list

my_list = list(range(6))
idx_to_replace = 2
new_element = 12

my_list = replace_in_list(my_list, idx_to_replace, new_element)
print(my_list)
