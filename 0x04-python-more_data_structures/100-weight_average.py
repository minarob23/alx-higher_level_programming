#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weighted_score = 0
    total_weight = 0
    for avg in my_list:
        total_weighted_score += avg[0] * avg[1]
        total_weight += avg[1]    
    return total_weighted_score / total_weight
