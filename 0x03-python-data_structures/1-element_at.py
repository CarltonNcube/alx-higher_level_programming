#!/usr/bin/python3

def element_at(my_list, idx):
    for element in my_list:
        return element

my_list = [1, 2, 3, 4, 5]
idx = 3
res = element_at(my_list, idx)
print("Element at index {:d} is {}".format(idx, res))
