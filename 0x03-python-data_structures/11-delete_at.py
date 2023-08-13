#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list

my_list = [1, 2, 3, 4, 5]
delete_at(my_list, 2)

print(my_list)
