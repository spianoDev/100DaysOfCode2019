# 6kyu on CodeWars: https://www.codewars.com/kata/598d89971928a085c000001a/train/python

# Introduction
# Little Petya very much likes sequences. Recently he has received one as a gift from his mother.
# Petya didn't like it at once. He decided to make a replacement.
# After the replacement Petya sorted the sequence by the numbers' non-decreasing.
# Now he is asking himself: What is the minimal possible value I could have got after the replacement and sorting the
# sequence?
#
# About the replacement
# Choose exactly one element from the sequence and replace it with another integer greater than 0.
# It is not allowed to replace a number with itself or to change no number at all.
#
# Task
# Find the minimal possible sequence after performing a valid replacement and sorting the sequence.
#
# Input:
# Input contains sequence with N integers. All elements of the sequence > 0. The sequenc will never be empty.
#
# Output:
# Return sequence with N integers the minimum possible values of each sequence element after one replacement and the sorting are performed.
#
# Examples:
#
# ([1,2,3,4,5])  =>  [1,1,2,3,4]
# ([4,2,1,3,5])  =>  [1,1,2,3,4]
# ([2,3,4,5,6])  =>  [1,2,3,4,5]
# ([2,2,2])      =>  [1,2,2]
# ([42])         =>  [1]

def sort_number(a):
    print(a)
# edge case of only 1 number in list
    if len(a) == 1 and a[0] != 1:
        a = [1]
        print(a)
        return a
    elif len(a) == 1 and a[0] == 1:
        a = [2]
        return a
# remove the last number from the list, make it 1 and insert it at the beginning of the list
    sort_a = sorted(a)
    if sort_a[-1] != 0:
        last = sort_a.pop(-1)
        last = 1
        sort_a.insert(0, last)
# edge case all numbers in list are 1
    count = 0
    for number in sort_a:
        if number != 1:
            count += 1
    if count > 0:
# return sorted list
        print(sort_a)
        return sort_a
    else:
        sort_a[-1] = 2
        print(sort_a)
        return sort_a

# sort_number([1,2,3,4,5]) # [1,1,2,3,4])
# sort_number([4,2,1,3,5]) # [1,1,2,3,4])
# sort_number([2,3,4,5,6]) # [1,2,3,4,5])
# sort_number([2,2,2]) # [1,2,2])
# sort_number([42]) # [1])
# sort_number([75, 70, 39, 46]) # [1, 39, 46, 70]
sort_number([1, 1, 1]) # [1, 1, 2]

