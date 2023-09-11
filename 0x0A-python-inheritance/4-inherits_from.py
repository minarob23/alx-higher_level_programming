#!/usr/bin/python3
""" Define function inherits_from"""
def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise, False.

    param obj: The object to check.
    param a_class: The class to compare with.
    Return:True if obj is an instance of a subclass of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    return False
