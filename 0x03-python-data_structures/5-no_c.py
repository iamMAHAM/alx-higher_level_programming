#!/usr/bin/python3

def no_c(my_string):
    output_string = []
    for i in range(len(my_string)):
        if my_string[i] in ['c', 'C']:
            pass
        else:
            output_string.append(my_string[i])
    return "".join(output_string)
