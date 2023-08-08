#!/usr/bin/python3
def uppercase(str):
    new_str=""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = ord(c) - 32
        else:
            c = ord(c)
        new_str += f"{c:c}"
    print(new_str)
