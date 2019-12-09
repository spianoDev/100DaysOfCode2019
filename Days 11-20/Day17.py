# 7kyu on CodeWars: https://www.codewars.com/kata/can-santa-save-christmas/train/python

# Can Santa save Christmas?
# Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own.
# But he has only 24 hours left. Can he do it?
# Your job is to determine if Santa can distribute all the presents in 24 hours.
#
# Your Task:
# You will get an array as input with time durations as string in the following format:
# "hh:mm:ss"
#
# Each duration is a present Santa has to distribute.
#
# Return true or false whether he can do it in 24 hours or not.

# since I have used this library before, I want to include the documentation for anyone wanting to know more about it
# https://docs.python.org/3/library/datetime.html
from datetime import time

def determineTime(arr):
    # I will need a way to grab each of the elements in the array so I can add them together
    total_hours = 0
    total_minutes = 0
    total_seconds = 0
    # I will need to loop through the different values: hours, minutes, and seconds
    for times in arr:
        # My first task is to get rid of the : so I can work with the numbers
        intervals = times.replace(":", "")
        # Next, I will use this logic: % 10 returns the final digit of a number. Dividing by 10 shifts the number one digit to the right.
        hour_tens = (int(intervals) // 100000) % 10
        hour_ones = (int(intervals) // 10000) % 10
        hours = (hour_tens * 10) + hour_ones
        minute_tens = (int(intervals) // 1000) % 10
        minute_ones = (int(intervals) // 100) % 10
        minutes = (minute_tens * 10) + minute_ones
        second_tens = (int(intervals) // 10) % 10
        second_ones = int(intervals) % 10
        seconds = (second_tens * 10) + second_ones
        # Finally I will need to consolidate the values to check if together they add up to more than 24 hours
        total_hours += hours
        total_minutes += minutes
        total_seconds += seconds
        if total_minutes > 60:
            total_minutes -= 60
            total_hours += 1
        print(intervals)
        print(total_hours)
        print(total_minutes)
        print(total_seconds)
        if total_hours >= 24:
            return False
        elif total_hours == 24 and total_minutes > 0:
            return False
        elif total_hours == 24 and total_seconds > 0:
            return False
    else:
        return True

print determineTime(["06:00:00", "18:00:00"])

