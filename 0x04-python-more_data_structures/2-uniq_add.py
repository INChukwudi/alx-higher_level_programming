#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for unique in set(my_list):
        result += unique
    return (result)
