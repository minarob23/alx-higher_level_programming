#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            try:
                formatted_item = "{:d}".format(item)
                print(formatted_item, end="")
                count += 1
                if count == x:
                    break
            except (ValueError, TypeError):
                continue
        print()
        return count
    except:
        return count
