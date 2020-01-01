# 6kyu on CodeWars: https://www.codewars.com/kata/greed-is-good/train/python

# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules.
# You will always be given an array with five six-sided dice values.
#
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet
# (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
#
# Example scoring
#
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   50 + 2 * 100 = 250
#  1 1 1 3 1   1000 + 100 = 1100
#  2 4 4 5 4   400 + 50 = 450

# As I started this process, I realized that it would take a very long time to go through every possible condition.
# Instead, I decided to sort the dice list into 6 new lists to facilitate scoring.
def score(dice):
    sum = 0
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    sixes = []
    for num in dice:
        if num == 1:
            ones.append(num)
        elif num == 2:
            twos.append(num)
        elif num == 3:
            threes.append(num)
        elif num == 4:
            fours.append(num)
        elif num == 5:
            fives.append(num)
        else:
            sixes.append(num)
# Next I'm going to look for any list that has a length of three or more to calculate those points
    if len(ones) >= 3:
        sum += 1000
    elif len(twos) >= 3:
        sum += 200
    elif len(threes) >= 3:
        sum += 300
    elif len(fours) >= 3:
        sum += 400
    elif len(fives) >= 3:
        sum += 500
    elif len(sixes) >= 3:
        sum += 600
# Finally, I need to look at the lists of 1s and 5s since they get points no matter what
    if len(ones) == 1:
        sum += 100
    elif len(ones) == 2:
        sum += 200
        # the case for 3 should be caught by the earlier if statement
    elif len(ones) == 4:
        sum += 100
    elif len(ones) == 5:
        sum += 200
    if len(fives) == 1:
        sum += 50
    if len(fives) == 2:
        sum += 100
    if len(fives) == 4:
        sum +=50
    if len(fives) == 5:
        sum +=100
    print(sum)
    return sum

score([2, 4, 4, 5, 4])
