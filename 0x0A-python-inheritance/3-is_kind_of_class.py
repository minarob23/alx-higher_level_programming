#!/usr/bin/python3
"""Define a function instance"""
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class; otherwise, False.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class or a subclass of it, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
