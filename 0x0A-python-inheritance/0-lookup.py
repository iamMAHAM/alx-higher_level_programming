#!/usr/bin/python3

"""print list of available attributes and methods of an object"""


def lookup(object):
    """return the list of attributes"""
    return dir(object)
