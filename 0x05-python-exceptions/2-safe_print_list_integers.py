#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        index = 0
        while count < x:
            item = my_list[index]
            try:
                formatted_item = "{:d}".format(item)
                print(formatted_item, end=" ")
                count += 1
            except (ValueError, TypeError):
                pass
            index += 1
    except IndexError:
        pass
    finally:
        print()
        return count
