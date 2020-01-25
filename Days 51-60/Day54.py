# 5kyu on CodeWars: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

# In this kata, you must create a digital root function.
# A digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until
# a single-digit number is produced. This is only applicable to the natural numbers.
#
# Here's how it works:
      #
      # digital_root(16)
      # => 1 + 6
      # => 7
      #
      # digital_root(942)
      # => 9 + 4 + 2
      # => 15 ...
      # => 1 + 5
      # => 6
      #
      # digital_root(132189)
      # => 1 + 3 + 2 + 1 + 8 + 9
      # => 24 ...
      # => 2 + 4
      # => 6
      #
      # digital_root(493193)
      # => 4 + 9 + 3 + 1 + 9 + 3
      # => 29 ...
      # => 2 + 9
      # => 11 ...
      # => 1 + 1
      # => 2
def digital_root(n):
    # I want to write a recursive loop that will continue the process until there is only one digit left
    # The edge case here is if n == 0
    if n == 0:
        return 0
    # first I need to make the number into a string so I can work with each digit separately
    string_number = str(n)
    while int(string_number) > 9:
        sum = 0
        # since I made the large number into a string, I can iterate over each digit
        for digit in string_number:
            print(digit)
            sum += int(digit)
            print(sum)
        # once I have the new sum I need to make that equal to the string_number to loop until there is one digit
        string_number = str(sum)
        print(sum)
    return sum

digital_root(493193)
