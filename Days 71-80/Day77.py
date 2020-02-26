# 6kyu on CodeWars: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second
# character of the final pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
# add the underscore if the length of the string is odd
    length = len(s)
    if length % 2 != 0:
        s = s + '_'
    print(s)
# split the string and pair up the result in pairs
    pairs = [(s[i:i+2]) for i in range(0, len(s), 2)]
    print(pairs)
# return result
    return pairs

# solution('abc') # ['ab', 'c_']
solution('abcdef') # ['ab', 'cd', 'ef']
