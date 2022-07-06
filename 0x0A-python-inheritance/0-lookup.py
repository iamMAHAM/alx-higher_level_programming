#!/usr/bin/python3

"""print list of available attributes and methods of an object"""


def lookup(object):
    return list(object.__dict__)
