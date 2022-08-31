#!?usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    weight = 0
    size = 0
    for (a, b) in my_list:
        weight += a * b
        size += b
    return (weight / size)
