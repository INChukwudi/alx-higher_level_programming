#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            copy.join(letter)
    return (copy)
