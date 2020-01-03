# 5kyu on CodeWars: https://www.codewars.com/kata/human-readable-time/train/python

# Write a function, which takes a non-negative integer (seconds) as input and returns the
# time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.

def make_readable(seconds):
    # I need to account for less than 10 seconds first so it will add the 0 before the number
    if seconds < 10:
        # zfill adds zeros to a string to fill a certain width.
        # In this case, I want to fill only 2 digits
        add_zero_to_seconds = str(seconds).zfill(2)
        return '00:00:' + str(add_zero_to_seconds)
    elif seconds < 60:
        return '00:00:' + str(seconds)
    elif seconds < 3600:
    # Now i need two conditionals for if the seconds are less than 10 and minutes less than 10
    # The double // gives an integer instead of a float which I also want
        if (seconds // 60) < 10:
            minutes = str(seconds // 60).zfill(2)
        else:
            minutes = seconds // 60
        if (seconds % 60) < 10:
            regular_seconds = str(seconds % 60).zfill(2)
        else:
            regular_seconds = str(seconds % 60)
        return '00:' + str(minutes) + ':' + str(regular_seconds)
    else:
        if seconds < 36000:
            hours = str(seconds // 3600).zfill(2)
        else:
            hours = str(seconds // 3600)
        if seconds % 3600 // 60 < 10:
            minutes = str(seconds % 3600 // 60).zfill(2)
        else:
            minutes = seconds % 3600 // 60
        if seconds % 3600 % 60 < 10:
            regular_seconds = str(seconds % 60).zfill(2)
        else:
            regular_seconds = str(seconds % 60)
        return str(hours) + ':' + str(minutes) + ':' + str(regular_seconds)


print(make_readable(60))
