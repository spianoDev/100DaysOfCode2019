# 6kyu on CodeWars: https://www.codewars.com/kata/permute-a-palindrome/train/python

# Write a function that will check whether the permutation of an input string is a palindrome.
# Bonus points for a solution that is efficient and/or that uses only built-in language functions.
# Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.
#
# Example
# madam -> True
# adamm -> True
# junk -> False
#
# Hint
# The brute force approach would be to generate all the permutations of the string and check each one of them whether it is a palindrome.
# However, an optimized approach will not require this at all.

# In looking at the hint and thinking about performance, a palindrome will only exist in the string if
# characters are repeated twice.
def permute_a_palindrome (input):
    not_a_pair = []
   # I'm going to sort the input first
    sorted_string = sorted(input)
   # Next I will compare each element and if there is a pair, delete both entries.
   # if it is a single add it to a new array
    while len(sorted_string) > 1:
        if sorted_string[0] == sorted_string[1]:
            del sorted_string[0:2]
        else:
            not_a_pair.append(sorted_string[0])
            del sorted_string[0:1]
    print(sorted_string)
    print(not_a_pair)
    # now i can compare the results for a final return to the problem
    if len(sorted_string) == 0 and len(not_a_pair) == 0:
        return True
    elif len(sorted_string) == 1 and len(not_a_pair) >= 1:
        return False
    elif len(sorted_string) == 0 and len(not_a_pair) >= 2:
        return False
    else:
        return True

permute_a_palindrome("baabcd")
