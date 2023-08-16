#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = rom_int.get(roman_string[0])

    for char in roman_string[1:]:
        if result < rom_int.get(char):
            result -= rom_int.get(char)
            result = abs(result)
            continue
        result += rom_int.get(char)

    return result
