#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            val1 = my_list_1[i] if i < len(my_list_1) else 0
            val2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                print("wrong type")
                result_list.append(0)
            elif val2 == 0:
                print("division by 0")
                result_list.append(0)
            else:
                result_list.append(val1 / val2)

        except IndexError:
            print("out of range")
            result_list.append(0)

    return result_list 
