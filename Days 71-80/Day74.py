# 6kyu on CodeWars: https://www.codewars.com/kata/5b7176768adeae9bc9000056/train/python
#
# Given a sorted array of distinct integers, write a function index_equals_value that returns the lowest index for which array[index] == index.
# Return -1 if there is no such index.
#
# Your algorithm should be very performant.
#
# [input] array of integers ( with 0-based nonnegative indexing )
# [output] integer
#
# Examples:
# input: [-8,0,2,5]
# output: 2 # since array[2] == 2
#
# input: [-1,0,3,6]
# output: -1 # since no index in array satisfies array[index] == index

def index_equals_value(arr):
    # loop through the values of the array
    for num in arr:
    # eliminate any array that has negative values
        if arr[-1] < 0:
            return -1
    # to help reduce the number of operations, I want to split the array
        half = len(arr)/2
        if num < half:
            if num == arr.index(num):
                print(' small ' + str(num))
                return num
        else:
            half_index = half
#             print('half index is ' + str(half_index))
            if num == arr.index(num):
                print('large ' + str(num))
                return num
    # need to return -1 when there isn't a match
    print('no match')
    return -1

# index_equals_value([-5, 1, 2, 3, 4, 5, 7, 10, 15]) # 1 (because the first index is the value 1)
index_equals_value([1,2,3,4,3,4,5,7]) # 7

# While this has significantly reduced the time in the fixed and edge cases, it is still timing out.
# I haven't gotten to the more advanced sorting techniques in my algorithm class, but I will return
# to this challenge when I cover them.
