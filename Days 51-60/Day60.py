# 6kyu on CodeWars: https://www.codewars.com/kata/5353212e5ee40d4694001114/train/python

# Array Exchange and Reversing
#
# It's time for some array exchange! The objective is simple: exchange the elements of two arrays in-place
# in a way that their new content is also reversed.
#
# # before
# my_list = ['a', 'b', 'c']
# other_list = [1, 2, 3]
#
# exchange_with(my_list, other_list)
#
# # after
# my_list == [3, 2, 1]
# other_list == ['c', 'b', 'a']

def exchange_with(a, b):
    print(a)
    print(b)
    new_a = []
    new_b = []
    for i, item in enumerate(reversed(b)):
        new_a.append(item)
    for i, item in enumerate(reversed(a)):
        new_b.append(item)
    a = new_a
    b = new_b
    print(a)
    print(b)


exchange_with(['a', 'b', 'c'], [1, 2, 3])
# This works perfectly, but I have no idea how to return the values to pass the tests which is super annoying!
