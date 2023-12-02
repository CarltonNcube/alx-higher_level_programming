#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    mid_idx = len(list_of_integers) // 2

    if (mid_idx == len(list_of_integers) - 1 or
            list_of_integers[mid_idx] >= list_of_integers[mid_idx + 1]) and \
            (mid_idx == 0 or
             list_of_integers[mid_idx] >= list_of_integers[mid_idx - 1]):
        return list_of_integers[mid_idx]

    if list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
        return find_peak(list_of_integers[:mid_idx])
    else:
        return find_peak(list_of_integers[mid_idx + 1:])
