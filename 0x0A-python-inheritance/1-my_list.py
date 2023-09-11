#!/usr/bin/python3
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public instance methods:
    - print_sorted(self): Prints the list in ascending sorted order without modifying the original list.
    
    Note: Assumes all elements in the list are of type int.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying the original list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
