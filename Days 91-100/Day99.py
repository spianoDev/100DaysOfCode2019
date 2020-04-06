# 6kyu on CodeWars: https://www.codewars.com/kata/55a5c82cd8e9baa49000004c/train/python

# Complete the function that takes 3 numbers x, y and k (where x <= y), and returns the number of integers within the
# range [x and y]
#  (both ends included) that are divisible by k.
#
# More scientifically: { i : x <= i <= y, i mod k = 0 }
#
# Example
# Given x = 6, y = 11, k = 2 the function should return 3, because there are three numbers divisible by 2 between 6 and 11: 6, 8, 10

def divisible_count(x,y,k):
# variable to hold the number of values
    count = 0
# loop through the numbers between x and y (inclusive) to determine which numbers are divisible by k
    while x <= y:
        if x % k == 0:
# if the remainder is 0, add to the count otherwise just increase x
            count += 1
            x += k
        else:
            x += 1
# return the total count
    print(count)
    return count

divisible_count(2, 100, 5)
# divisible_count(6,11,2) #3
# divisible_count(101,99999999,11)
