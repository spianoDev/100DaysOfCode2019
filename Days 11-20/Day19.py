# 7kyu on CodeWars: https://www.codewars.com/kata/holiday-ii-plane-seating/train/python

# Finding your seat on a plane is never fun, particularly for a long haul flight...
# You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.
#
# To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.
#
# the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is
# (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.
#
# Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.
#
# Given a seat number, your task is to return the seat location in the following format:
#
# '2B' would return 'Front-Left'.
#
# If the number is over 60, or the letter is not valid, return 'No Seat!!'.

def plane_seat(seat):
    # First I need to separate the number and the letter from the seat assignment
    print(list(seat))
    # Then I need variables for each value so I can use the information
    if len(list(seat)) == 2:
        seat_number = list(seat)[0]
        seat_letter = list(seat)[1]
    else:
        seat_number = list(seat)[0] + list(seat)[1]
        seat_letter = list(seat)[2]
    print(seat_number)
    print(seat_letter)
    # Now I need to set the conditionals for the location of the seat
    if int(seat_number) > 60 or seat_letter == 'I' or seat_letter == 'J':
                   return 'No Seat!!'
    elif int(seat_number) > 40 and seat_letter == 'A' or int(seat_number) > 40 and seat_letter == 'B' or int(seat_number) > 40 and seat_letter == 'C':
        return 'Back-Left'
    elif int(seat_number) > 40 and seat_letter == 'D' or int(seat_number) > 40 and seat_letter == 'E' or int(seat_number) > 40 and seat_letter == 'F':
        return 'Back-Middle'
    elif int(seat_number) > 40 and seat_letter == 'G' or int(seat_number) > 40 and seat_letter == 'H' or int(seat_number) > 40 and seat_letter == 'K':
        return 'Back-Right'
    elif int(seat_number) > 20 and seat_letter == 'A' or int(seat_number) > 20 and seat_letter == 'B' or int(seat_number) > 20 and seat_letter == 'C':
        return 'Middle-Left'
    elif int(seat_number) > 20 and seat_letter == 'D' or int(seat_number) > 20 and seat_letter == 'E' or int(seat_number) > 20 and seat_letter == 'F':
        return 'Middle-Middle'
    elif int(seat_number) > 20 and seat_letter == 'G' or int(seat_number) > 20 and seat_letter == 'H' or int(seat_number) > 20 and seat_letter == 'K':
        return 'Middle-Right'
    elif seat_letter == 'A' or seat_letter == 'B' or seat_letter == 'C':
         return 'Front-Left'
    elif seat_letter == 'D' or seat_letter == 'E' or seat_letter == 'F':
         return 'Front-Middle'
    elif seat_letter == 'G' or seat_letter == 'H' or seat_letter == 'K':
         return 'Front-Right'

print plane_seat('20B')
