# 5kyu on CodeWars: https://www.codewars.com/kata/529872bdd0f550a06b00026e/train/python

# Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits in the given string of digits.
#
# For example:
#
# greatestProduct("123834539327238239583") // should return 3240
# The input string always has more than five digits.

def greatest_product(n):
# need two pointers to compare chunks of products and a product variable
    pointer1 = 4
    biggest_product = 0
    last_index = len(n) - 1
# loop through digits of n
    while pointer1 <= last_index:
        for digit in n:
            product = int(n[pointer1]) * int(n[pointer1 - 1]) * int(n[pointer1 - 2]) * int(n[pointer1 - 3]) * int(n[pointer1 - 4])
            pointer1 += 1
# if the product is greater than the variable value, update the variable
            if biggest_product < product:
                biggest_product = product
#                 print(pointer1)
#                 print(biggest_product)
                break
            else:
#                 print(pointer1)
#                 print(biggest_product)
                break
    print(biggest_product)
    return biggest_product

greatest_product("123834539327238239583") # 3240
# greatest_product("92494737828244222221111111532909999") # 5292
# greatest_product("02494037820244202221011110532909999") # 0
