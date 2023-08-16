#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    k = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary.get(k):
            k = key
    return k or None
