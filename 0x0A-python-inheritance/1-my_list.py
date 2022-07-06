#!/usr/bin/python3

"""module for Mylist class"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """print a sorted list in ascending order"""
        print(sorted(self))
