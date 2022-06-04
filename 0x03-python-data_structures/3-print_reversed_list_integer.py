#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[-i])) if (i != 0) else 0
    print("{:d}".format(my_list[0]))
