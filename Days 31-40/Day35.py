# 6kyu on CodeWars: https://www.codewars.com/kata/find-the-parity-outlier/train/python

# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
# First I will loop through all the numbers to make two new lists: an even and an odd
    even_ints = []
    odd_ints = []
    for nums in integers:
    # I will use the remainder to determine if the numbers are even or odd
        if nums % 2  == 0:
            # then I will add the numbers into the new lists
            even_ints.append(nums)
        else:
            odd_ints.append(nums)
    # Now I need to determine which list has a length of 1 and return the only value in the list
    if len(even_ints) == 1:
        return even_ints[0]
    else:
        return odd_ints[0]

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
