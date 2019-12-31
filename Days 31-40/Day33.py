# 7kyu on CodeWars: https://www.codewars.com/kata/breaking-chocolate-problem/train/python

# Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable.
# Implement a function that will return minimum number of breaks needed.
#
# For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.
#
# If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.

# So before starting out, I was working out anticipated answers. I think all I need to do is multiply the two
# dimensions and subtract one.

def breakChocolate(n, m):
# my instinct was correct, but I need a condition for if the answer is less than 0
    answer = (n * m) - 1
    if answer <= 0:
        return 0
    return answer

print(breakChocolate(0,0))
