#!/usr/bin/python3

elem = 0
def safe_print_list(my_list=[], x=0):
    for index in range(x):
        try:
            print(f"{my_list[index]}", end="")
            elem += 1
        except IndexError:
            break
    print("")
    return (elem)
