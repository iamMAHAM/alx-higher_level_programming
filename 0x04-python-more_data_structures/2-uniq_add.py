#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for item in my_list:
        sum += item if item not in new_list else 0
        new_list.append(item)
    return sum
