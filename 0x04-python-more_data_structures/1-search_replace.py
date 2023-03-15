#!/usr/bin/python3


"""
    function that replaces all occurrences of an element
    by another in a new list.
"""


def search_replace(my_list, search, replace):
    new = my_list[:]
    for i in range(len(my_list) - 1):
        if my_list[i] == search:
            new[i] = replace
    return new
