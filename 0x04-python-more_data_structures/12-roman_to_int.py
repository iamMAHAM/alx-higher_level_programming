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


roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))