#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            
            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                raise TypeError("wrong type")
            
            if divisor == 0:
                raise ZeroDivisionError("division by 0")
            
            result = dividend / divisor
            result_list.append(result)
            
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except TypeError:
            print("wrong type")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
    
    return result_list
