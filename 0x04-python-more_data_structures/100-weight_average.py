#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sc_we = 0
    av = 0

    for tup in my_list:
        sc_we += tup[0] * tup[1]
        av += tup[1]

    return (sc_we / av)
