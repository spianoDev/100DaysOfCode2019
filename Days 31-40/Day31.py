# 8kyu on CodeWars: https://www.codewars.com/kata/what-is-between/train/python

# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers
# between the input parameters, including them.
#
# For example:
#
# a = 1
# b = 4
# --> [1, 2, 3, 4]

def between(a,b):
# first I need a variable to put the list
    answer = []
    # now I will use a for loop to collect all the numbers between the two numbers.
    # I have to add 1 to the second number so it will also be included
    for num in range(a, (b + 1), 1):
    # now I add each number to the list
        answer.append(num)
    return answer
print(between(1, 4))
