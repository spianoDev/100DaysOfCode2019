# 6kyu on CodeWars: https://www.codewars.com/kata/how-many-reindeers/train/python

# Santa puts all the presents into the huge sack. In order to let his reindeers rest a bit, he only takes as many reindeers with him as he is required to do. The others may take a nap.
#
# Two reindeers are always required for the sleigh and Santa himself. Additionally he needs 1 reindeer per 30 presents. As you know, Santa has 8 reindeers in total, so he can deliver up to 180 presents at once (2 reindeers for Santa and the sleigh + 6 reindeers with 30 presents each).
#
# Complete the function reindeers(), which takes a number of presents and returns the minimum numbers of required reindeers. If the number of presents is too high, throw an error.
#
# Examles:
#
# reindeer(0) # must return 2
# reindeer(1) # must return 3
# reindeer(30) # must return 3
# reindeer(200) # must throw an error

def reindeer(presents):
# since you need 2 reindeer just to pull Santa...
    reindeer_needed = 2
    if presents == 0:
        return reindeer_needed
# and one additional reindeer for every 30 presents
    elif presents <= 30:
        reindeer_needed += 1
        return reindeer_needed
    elif presents <= 60:
        reindeer_needed += 2
        return reindeer_needed
    elif presents <= 90:
        reindeer_needed += 3
        return reindeer_needed
    elif presents <= 120:
        reindeer_needed += 4
        return reindeer_needed
    elif presents <= 150:
        reindeer_needed += 5
        return reindeer_needed
    elif presents <= 180:
        reindeer_needed += 6
        return reindeer_needed
   # but cannot go over 6 reindeer or it should throw an error
    else:
        raise Exception('error')

print reindeer(181)
