#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = []
    for item in set_1:
        diff.append(item) if item not in set_2 else 0

    for item2 in set_2:
        diff.append(item2) if item2 not in set_1 else 0
    return diff
