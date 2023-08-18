#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is None or type(roman_string) is not str:
        return 0

    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }

    result = 0
    prev_num = 0

    for char in reversed(roman_string):
        num = roman_numerals[char]
        if num >= prev_num:
            result += num

        else:
            result -= num
        prev_num = num

    return result
