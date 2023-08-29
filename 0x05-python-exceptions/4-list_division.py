#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            
            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                raise TypeError("wrong type")
            
            if divisor == 0:
                raise ZeroDivisionError("division by 0")
            
            result = dividend / divisor
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        
        result_list.append(result)
    
    return result_list
