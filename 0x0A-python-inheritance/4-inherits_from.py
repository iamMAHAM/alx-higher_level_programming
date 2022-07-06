#!/usr/bin/python3

"""module 4"""


def inherits_from(obj, a_class):
    "inherit"
    return issubclass(type(obj), a_class) and type(obj) != a_class
