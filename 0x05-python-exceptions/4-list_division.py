#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            
            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                result = dividend / divisor
            else:
                result = 0
                raise TypeError("wrong type")
            
            result_list.append(result)
            
        except ZeroDivisionError:
            result_list.append(0)
            print("division by 0")
        except TypeError:
            result_list.append(0)
            print("wrong type")
        except IndexError:
            result_list.append(0)
            print("out of range")
    
    return result_list

