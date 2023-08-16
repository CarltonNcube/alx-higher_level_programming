#!/usr/bin/python3

def uniq_add(my_list=[]):
    output = []
    for i in my_list:
        if i not in output:
            output.append(i)
    return sum(output) 
