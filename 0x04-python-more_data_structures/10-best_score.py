#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or not isinstance(a_dictionary, dict):
        return None

    key_0 = list(a_dictionary.keys())[0]
    largest = a_dictionary[key_0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > largest:
            largest = a_dictionary[key]
            key_0 = key
    return (key_0)
