#!/usr/bin/python3
def element_at(my_list, idx):
    return my_list[idx]
 
my_list = [1, 2, 3]
idx = 1
result = element_at(my_list, idx)
print("Element at index {:d} is {}".format(idx, result))
