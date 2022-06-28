#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """ Unit cases for max_integer """
    
    def empty(self):
        self.assertIs(max_integer(), None)

    def negative_list(self):
        self.assertIs(max_integer([-7, -4, -9]), -4)

    def max_normal(self):
        self.assertIs(max_integer([50, 38, 29, 60, 25, 6]), 60)

    def none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def string_argument(self):
        self.assertIs(max_integer("Alx SE engineering program"), "x")

    def list_string(self):
        with self.assertRaises(TypeError):
            max_integer(["alx", 0])

    def one_element(self):
        self.assertIs(max_integer([1]), 1)

if __name__ == "__main__":
    unittest.main()
