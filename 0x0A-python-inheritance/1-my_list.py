#!/usr/bin/python3
"""A custom list class that inherits from the built-in list class."""
class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying the original list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
