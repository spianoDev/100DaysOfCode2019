# 6kyu on CodeWars: https://www.codewars.com/kata/5365bb5d5d0266cd010009be/train/python

# Making Change
# Complete the method that will determine the minimum number of coins needed to make change for a given amount in American currency.
#
# Coins used will be half-dollars, quarters, dimes, nickels, and pennies, worth 50cents, 25, 10, 5 and 1, respectively.
# They'll be represented by the symbols H, Q, D, N and P (symbols in Ruby, strings in in other languages)
#
# The argument passed in will be an integer representing the value in cents.
# The return value should be a hash/dictionary/object with the symbols as keys, and the numbers of coins as values.
# Coins that are not used should not be included in the hash.
# If the argument passed in is 0, then the method should return an empty hash.
#
# Examples
# make_change(0)   -->  {}
# make_change(1)   -->  {"P":1}
# make_change(43)  -->  {"Q":1, "D":1, "N":1, "P":3}
# make_change(91)  -->  {"H":1, "Q":1, "D":1, "N":1, "P":1}

def make_change(amount):
    # I will start with the edge case of 0
    if amount == 0:
        result = {}
        return result
    # I think I can accomplish this by using a bunch of if/else statements
    # I need to make a lists of the possible coin values
    coin_values = ["H", "Q", "D", "N", "P"]
    # Then I need the number of each type of coin (initialize as 0)
    num_coin = [0, 0, 0, 0, 0]
    if amount > 0:
        # the values of each coin type
        half_dollars = amount // 50
        quarters = amount % 50 // 25
        dimes = (amount - (half_dollars * 50) - (quarters * 25)) // 10
        nickels = (amount - (half_dollars * 50) - (quarters * 25) - (dimes * 10)) // 5
        pennies = (amount - (half_dollars * 50) - (quarters * 25) - (dimes * 10) - (nickels * 5))
        # assign these values to each key for the dictionary
        num_coin[0] = half_dollars
        num_coin[1] = quarters
        num_coin[2] = dimes
        num_coin[3] = nickels
        num_coin[4] = pennies
        # The result is the mixing of the two lists in key/value pairs
        result = dict(zip(coin_values, num_coin))
        # The new_result eliminates any value of 0 in the final return
        new_result = {k:v for k,v in result.items() if not v == 0}
        print(new_result)
        return new_result

print(make_change(1)) # {"P": 1}
# print(make_change(43)) # {"Q": 1, "D": 1, "N": 1, "P": 3}
print(make_change(91)) # {"H": 1, "Q": 1, "D": 1, "N": 1, "P": 1}
