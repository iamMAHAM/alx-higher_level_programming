#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    values = []
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for val in a_dictionary.values():
        max = val if val > max else max
    values = list(a_dictionary.values())
    return list(a_dictionary.keys())[values.index(max)]
