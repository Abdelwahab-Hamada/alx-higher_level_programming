#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sum_result = 0

    for el in uniq_list:
        sum_result += el

    return (sum_result)
