# 6kyu on CodeWars: https://www.codewars.com/kata/is-integer-array/train/python

# Write a function with the signature shown below:
#
# def is_int_array(arr):
#     return True
# returns true / True if every element in an array is an integer or a float with no decimals.
# returns true / True if array is empty.
# returns false / False for every other input.

def is_int_array(arr):
    # I'm going to make a new list for numbers only
    number_list = []
    # This passed the tests, but I had to add an additional conditional because of an exit code error
    if arr == None or arr == '':
        return False
    #first I will eliminate non-number arguments
    for num in arr:
        if isinstance(num, str) or num == None:
            return False
        # now I need to differentiate between floats ending in 0 and those with numbers later
        elif isinstance(num, float):
            if num == int(num):
                number_list.append(num)
            else:
                return False
        elif isinstance(num, int):
            number_list.append(num)
    print(number_list)
    return True
print(is_int_array([1.0, 2.0, None]))


