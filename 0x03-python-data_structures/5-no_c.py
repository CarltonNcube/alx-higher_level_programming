#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

print(no_c("Carlton"))
print(no_c("Coding is fun!"))
print(no_c("Removing character C"))
