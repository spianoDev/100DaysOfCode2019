# 7kyu on CodeWars: https://www.codewars.com/kata/naughty-or-nice-2/train/python

# In this kata, you will write a function that receives an array of string and returns a string that is either 'naughty' or 'nice'.
# Strings that start with the letters b, f, or k are naughty.
# Strings that start with the letters g, s, or n are nice.
# Other strings are neither naughty nor nice.
#
#   If there is an equal amount of bad and good actions, return 'naughty'
#
#   Examples:
#
#   bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
#   whatListAmIOn(bad_actions)
#   #-> 'naughty'
#   good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
#   what_list_am_i_on(good_actions)
#   #-> 'nice'
#   actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
#   what_list_am_i_on(actions)
#   #-> 'naughty'
def what_list_am_i_on(actions):
# I will need a place to store the strings as they are sorted into 'naughty' or 'nice'
    nice = []
    naughty = []
# first I need to loop through the different string values
    for string in actions:
    # next create if statement for the 'naughty' list
        if string.startswith('b', 0, 1) or string.startswith('f', 0, 1) or string.startswith('k', 0, 1):
            naughty.append(string)
    # then create else statement for the 'nice' list
        elif string.startswith('g', 0, 1) or string.startswith('s', 0, 1) or string.startswith('n', 0, 1):
            nice.append(string)
    print(nice)
    print(naughty)
    # finally I need a conditional for the sorted lists.
    if len(nice) > len(naughty):
        return 'nice'
    elif len(nice) < len(naughty) or len(nice) == len(naughty):
        return 'naughty'

actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes', 'broke someone\'s window', 'fought over a toaster', 'killed a bug']
print what_list_am_i_on(actions)
