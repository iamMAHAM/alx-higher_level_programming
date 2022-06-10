#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    a = 0
    b = 0
    for item in my_list:
        t_list = list(item)
        a += t_list[0] * t_list[1]
        b += t_list[1]

    return a / b
