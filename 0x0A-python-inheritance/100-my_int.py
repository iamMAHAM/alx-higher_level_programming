#!/usr/bin/python3
"""Module 100"""


class MyInt(int):
    """Rebel class"""

    def __eq__(self, n):
        """Override == operator"""
        return not (self is not n)

    def __ne__(self, n):
        """Override != operator"""
        return (self is not n)
