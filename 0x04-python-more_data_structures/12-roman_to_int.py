#!/usr/bin/python3


def roman_to_int(roman_string):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0

    if type(roman_string) != str or roman_string is None:
        return output

    behind = None
    for letter in roman_string:
        if letter not in numbers.keys():
            pass
        else:
            number = numbers.get(letter)
            if behind is None:
                output = number
                behind = number
                continue
            elif behind < number:
                output = output + number - behind * 2
            else:
                output += number

            behind = number

    return output
