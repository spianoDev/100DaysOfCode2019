# 5kyu on CodeWars:

# We all know about Roman Numerals, and if not, here's a nice introduction kata. And if you were anything like me, you 'knew' that the numerals were not used for zeroes or fractions; but not so!
#
# I learned something new today: the Romans did use fractions and there was even a glyph used to indicate zero.
#
# So in this kata, we will be implementing Roman numerals and fractions.
#
# Although the Romans used base 10 for their counting of units, they used base 12 for their fractions. The system used dots to represent twelfths, and an S to represent a half like so:
#
# 1/12 = .
# 2/12 = :
# 3/12 = :.
# 4/12 = ::
# 5/12 = :.:
# 6/12 = S
# 7/12 = S.
# 8/12 = S:
# 9/12 = S:.
# 10/12 = S::
# 11/12 = S:.:
# 12/12 = I (as usual)
# Further, zero was represented by N
#
# Kata
# Complete the method that takes two parameters: an integer component in the range 0 to 5000 inclusive, and an optional fractional component in the range 0 to 11 inclusive.
#
# You must return a string with the encoded value. Any input values outside the ranges given above should return "NaR" (i.e. "Not a Roman" :-)
#
# Examples
# roman_fractions(-12)     #=> "NaR"
# roman_fractions(0, -1)   #=> "NaR"
# roman_fractions(0, 12)   #=> "NaR"
# roman_fractions(0)       #=> "N"
# roman_fractions(0, 3)    #=> ":."
# roman_fractions(1)       #=> "I"
# roman_fractions(1, 0)    #=> "I"
# roman_fractions(1, 5)    #=> "I:.:"
# roman_fractions(1, 9)    #=> "IS:."
# roman_fractions(1632, 2) #=> "MDCXXXII:"
# roman_fractions(5000)    #=> "MMMMM"
# roman_fractions(5001)    #=> "NaR"

# I'm going to expand upon the work I did in Day78 for this solution

def roman_fractions(integer, fraction=None):
# edge cases of less than 0 or more than 5000
    if integer < 0 or integer > 5000:
        print('NaR')
        return 'NaR'
# create a dictionary of all the different roman values...
    roman_chars = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
     20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
     200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
     2000: 'MM', 3000: 'MMM', 4000: 'MMMM', 5000: 'MMMMM'}
# create a dictionary of all the different fractional symbols...
    fractions_roman = {0: '', 1: '.', 2: ':', 3: ':.', 4: '::', 5: ':.:', 6: 'S', 7: 'S.', 8: 'S:', 9: 'S:.',
    10: 'S::', 11: 'S:.:'}
# create a variable that I can add roman symbols to
    pieces = []
# make variables that will separate each digit so I can access them from the dictionary
    thousands = integer // 1000
    hundreds = integer // 100 % 10
    tens = integer // 10 % 10
    ones = integer % 10
    print(thousands, hundreds, tens, ones)
# edge case for integer = zero
    if integer == 0 and fraction is None or integer == 0 and fraction == 0:
        print('N')
        return 'N'
# use the roman_chars dictionary to grab the values in order from thousands to hundreds to tens to ones
    if thousands > 0:
        thousands *= 1000
        pieces.append(roman_chars[thousands])
    if hundreds > 0:
        hundreds *= 100
        pieces.append(roman_chars[hundreds])
    if tens > 0:
        tens *= 10
        pieces.append(roman_chars[tens])
    if ones > 0:
        pieces.append(roman_chars[ones])
# use the fractions_roman dictionary to grab the fractional
    print(fraction)
# edge cases of non-existent fractional (tried fraction != None but the testing didn't like that)
    if fraction is None:
        answer = "".join(pieces)
        print(answer)
        return answer
    elif fraction < 0 or fraction >= 12:
        print('NaR')
        return 'NaR'
    elif fraction >= 0 and fraction < 12:
        pieces.append(fractions_roman[fraction])
    print(pieces)
    answer = "".join(pieces)
    print(answer)
    return answer

# roman_fractions(-12) # "NaR"
# roman_fractions(0, -1) # "NaR"
# roman_fractions(0, 12) # "NaR"
# roman_fractions(0) # "N"
# roman_fractions(1) # "I"
# roman_fractions(1, 5) # "I:.:"
# roman_fractions(1, 9) # "IS:."
# roman_fractions(1632, 2) # "MDCXXXII:"
# roman_fractions(5000) # "MMMMM"
# roman_fractions(5001) # "NaR"
roman_fractions(0, 0)
