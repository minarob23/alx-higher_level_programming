#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
    return result
