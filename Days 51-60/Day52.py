# 6kyu on CodeWars: https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python

# Write a simple parser that will parse and run Deadfish.
#
# Deadfish has 4 commands, each 1 character long:
#
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.
#
# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    num = 0
    return_arr = []
    for char in data:
        if char == 'i':
            num += 1
        elif char == 'd':
            num -= 1
        elif char == 's':
            num *= num
        elif char == 'o':
            return_arr.append(num)
    print(return_arr)
    return return_arr

print(parse("ioioio"))
