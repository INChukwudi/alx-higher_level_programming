#!/usr/bin/python3
def no_c(my_string):
    copy = [s for s in my_string if s != 'c' and s != 'C']
    return ("".join(copy))
