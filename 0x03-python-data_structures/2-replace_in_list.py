#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
         return list(my_list)
    else:
        new_list = list(my_list)
        new_list[idx] = element
        return new_list

my_list = list(range(1 ,6))
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
