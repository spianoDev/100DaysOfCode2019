# 8kyu on CodeWars: https://www.codewars.com/kata/count-the-monkeys/train/python

# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is
# too young to just appreciate the full number, he has to start counting them from 1.
#
# As a good parent, you will sit and count with him. Given the number (n), populate an array
# with all numbers up to and including that number, but excluding zero.
#
# For example:
#
# monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# monkeyCount(1) # --> [1]

def monkey_count(n):
    answer = []
# I need to just add from 1 through 'n + 1' to a new array to count
    for count in range(1, (n+1)):
        answer.append(count)
    return answer
print(monkey_count(10))
