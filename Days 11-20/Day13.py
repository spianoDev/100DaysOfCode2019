# 7kyu on CodeWars: https://www.codewars.com/kata/countdown-to-christmas/train/python

# Polly is 8 years old. She is eagerly awaiting Christmas as she has a bone to pick with Santa Claus. Last year she asked for a horse, and he brought her a dolls house. Understandably she is livid.

# The days seem to drag and drag so Polly asks her friend to help her keep count of how long it is until Christmas,
# in days. She will start counting from the first of December.

# Your function should take 1 argument (a Date object) which will be the day of the year it is currently. The function
# should then work out how many days it is until Christmas.

# Watch out for leap years!

# I'm going to start by importing the date method for python
from datetime import date

def days_until_christmas(day):
    # there is a handy built in method that will convert the date into the day number of the year. That is what I
    # will use to determine the remaining days until Christmas.
    if day.year % 4 == 0:
        christmas = 360
    else:
        christmas = 359
    days = day.strftime('%j')
    num_days = christmas - int(days)
    print(num_days)
    # my first round of testing this I didn't take into account that the number returned could be a negative number.
    # This should correct that issue.
    if christmas == 359 and num_days == 365 or christmas == 360 and num_days == 366:
        return 0
    elif num_days > 0:
        return num_days
    elif num_days < 0:
        if day.year % 4 == 3:
        # meaning the following year is a leap year.
            num_days += 366
        else:
            num_days += 365
    return num_days
print days_until_christmas(date(1900,11,5))
