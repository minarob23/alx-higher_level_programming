#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    for i in my_list:
        if my_list[i] > my_list[max]:
            max = i
        return my_list[max]
