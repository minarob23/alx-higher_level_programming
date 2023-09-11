#!/usr/bin/python3
"""This function returns a list of available attributes and methods of an object."""
def lookup(obj):
   """ obj: The object to inspect."""
    return dir(obj)
