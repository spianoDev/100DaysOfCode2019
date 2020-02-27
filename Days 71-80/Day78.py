# Beta on CodeWars: https://www.codewars.com/kata/5580d8dc8e4ee9ffcb000050/train/python

# The magazine staff is asking us to help them with the issue numbers.
# Magazines are numbered using Roman Numerals.
#
# We need to be able to convert Arabic numerals to Roman ones.
#
# Initially our API only needs to support numbers from 1 to 999.
#
# The API must manage nonconvertible numbers by returning the Not a Roman constant string "NaR".
#
# Examples:
# Given
#
# arabic_to_roman(0) # => "NaR"
# arabic_to_roman(-1) # => "NaR"
# arabic_to_roman(1) # => "I"
# arabic_to_roman(5) # => "V"
# arabic_to_roman(599) # => "DXCIX"

def arabic_to_roman(arabic):
# edge cases of less than 0 or more than 999
    if arabic < 1 or arabic > 999:
        print('NaR')
        return 'NaR'
# create a dictionary of all the different roman values...
# The tricky part is dealing with the 4 and 9 cases since they require subtraction
    roman_chars = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
     20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
     200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM'}
# create a variable that I can add values to
    pieces = []
# make variables that will separate each digit so I can access them from the dictionary
    hundreds = arabic // 100
    tens = arabic // 10
    ones = arabic % 10
    print(hundreds, tens, ones)
# use the dictionary to grab the values in order from hundreds to tens to ones
    if hundreds > 0:
        hundreds *= 100
        pieces.append(roman_chars[hundreds])
    if tens > 0:
        if tens < 10:
            tens *= 10
            pieces.append(roman_chars[tens])
        else:
            tens = tens % 10
            if tens > 0:
                tens *= 10
                pieces.append(roman_chars[tens])
    if ones > 0:
        pieces.append(roman_chars[ones])
    print(pieces)
    answer = "".join(pieces)
    print(answer)
    return answer


#
# arabic_to_roman(-1) # "NaR"
# arabic_to_roman(0) # "NaR"
# arabic_to_roman(1000) # "NaR"
# arabic_to_roman(3) # "III"
# arabic_to_roman(4) # "IV"
# arabic_to_roman(5) # "V"
# arabic_to_roman(6) # "VI"
# arabic_to_roman(23) # 'XXIII'
arabic_to_roman(100)
# arabic_to_roman(599) # "DXCIX"
