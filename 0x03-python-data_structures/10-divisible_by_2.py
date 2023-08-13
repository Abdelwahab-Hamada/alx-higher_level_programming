#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    l = []
    for i in my_list:
        l.append(not(bool(i % 2)))

    return (l)
