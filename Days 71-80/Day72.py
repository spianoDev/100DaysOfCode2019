# 5kyu on CodeWars: https://www.codewars.com/kata/5ae43ed6252e666a6b0000a4/train/python

# Welcome
# This kata is inspired by This Kata
#
# We have a string s
#
# We have a number n
#
# Here is a function that takes your string, concatenates the even-indexed chars to the front, odd-indexed chars to the back.
#
# Examples
# s = "Wow Example!"
# result = "WwEapeo xml!"
# s = "I'm JomoPipi"
# result = "ImJm ii' ooPp"
# The Task:
# return the result of the string after applying the function to it n times.
#
# example where s = "qwertyuio" and n = 2:
#
# after 1 iteration  s = "qetuowryi"
# after 2 iterations s = "qtorieuwy"
# return "qtorieuwy"
# Note
# there's a lot of tests, big strings, and n is greater than a billion
#
# so be ready to optimize.

# def jumbled_string(s, n):
#     # everything gets wrapped in a recursive loop to run n times
#     while n > 0:
#     # I'm going to need two new variables to store the odd/even characters
#         even_front = []
#         odd_back = []
#         for index, char in enumerate(s):
#             if index % 2 == 0:
#                 even_front.append(char)
#             else:
#                 odd_back.append(char)
# #         print(even_front, odd_back)
#         # Then concatenate the two joined arrays together
#         answer = "".join(even_front) + "".join(odd_back)
# #         print(answer)
#         s = answer
#         n -= 1
#         if n == 0:
#             print(answer)
#             return answer

# The above answer totally works, but it isn't efficient to pass all the tests

def jumbled_string(s, n):
    # everything gets wrapped in a recursive loop to run n times
    while n > 0:
    # I'm going to need two new variables to store the odd/even characters
    # This time I am grabbing every other index using the python string range
        even_front = s[0:len(s):2]
        odd_back = s[1:len(s):2]
        # Then concatenate the variables together
        answer = even_front + odd_back
#         print(answer)
        s = answer
        n -= 1
        if n == 0:
            print(answer)
            return answer

# this answer is much faster, but still times out

# jumbled_string("Such Wow!", 1) # "Sc o!uhWw"
# jumbled_string("qwertyuio", 2) # "qtorieuwy"
# jumbled_string("better example", 2) # "bexltept merae"
jumbled_string("Greetings", 8) # "Gtsegenri"


