# 5kyu on CodeWars: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(string):
    print(string)
# edge case of str == ""
    if len(string) == 0:
        return '1'
# variables for return values
    letters = []
    numbers = []
# I need to separate the alpha from the numeric values
    for char in string:
        if char.isalpha():
            letters.append(char)
        if char.isdigit():
            numbers.append(char)
# increment the number by 1
    if len(numbers) == 0:
        numbers.append('1')
# need a loop to look for all instances of '9' starting from the end of the list
    else:
        if int(numbers[-1]) < 9:
            print(int(numbers[-1]))
            increment = int(numbers[-1]) + 1
            print(increment)
            numbers.insert(-1, str(increment))
            numbers.pop(-1)
        else:
            nine_count = 0
            for i, num in enumerate(reversed(numbers)):
#                 print(i, num)
                if int(num) == 9 and i <= nine_count:
                    nine_count += 1
                    numbers[-1 - i] = '0'
                elif int(num) < 9 and i <= nine_count:
                    numbers[-1 - i] = int(num) + 1
                    numbers[-1 - i] = str(numbers[-1 - i])
            if int(numbers[0]) == 0 and len(numbers) <= nine_count:
                numbers.insert(0, '1')
    print(letters)
    print(numbers)
# join the string together again and return it
    answer = "".join(letters) + "".join(numbers)
    print(answer)
    return answer

# increment_string("foo")
# => foo1
# increment_string("foobar001")
# => foobar002
# increment_string("foobar0199")
# => foobar0200
# increment_string("")
# => 1
# increment_string('123')
# => 124
# increment_string('foo9')
# => foo10
# increment_string('bar09')
# => bar10
# increment_string('009229')
# => 009230
increment_string('KC020489Gco!93357239301')

