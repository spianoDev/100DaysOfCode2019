# 5kyu on CodeWars: https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d/train/python

# You work at a taxi central.
# People contact you to order a taxi. They inform you of the time they want to be picked up and dropped off.
#
# A taxi is available to handle a new customer 1 time unit after it has dropped off a previous customer.
#
# What is the minimum number of taxis you need to service all requests?
#
# Constraints:
# Let N be the number of customer requests:
# N is an integer in the range [1, 100k]
# All times will be integers in range [1, 10k]
# Let PU be the time of pickup and DO be the time of dropoff
# Then for each request: PU < DO
# The input list is NOT sorted.
# Examples:
# # Two customers, overlapping schedule. Two taxis needed.
# # First customer wants to be picked up 1 and dropped off 4.
# # Second customer wants to be picked up 2 and dropped off 6.
# requests = [(1, 4), (2, 6)]
# min_num_taxis(requests) # => 2
#
# # Two customers, no overlap in schedule. Only one taxi needed.
# # First customer wants to be picked up 1 and dropped off 4.
# # Second customer wants to be picked up 5 and dropped off 9.
# requests = [(1, 4), (5, 9)]
# min_num_taxis(requests) # => 1

# I have decided to start over and go in a different direction

def min_num_taxis(requests):
    # before I start comparisons, I can eliminate edge cases
    # Unless empty, 1 taxi will always be required
    if len(requests) == 0:
        return 0
    if len(requests) == 1:
        return 1
    # I am going to start by sorting the values but I need a new function to do that
    # I realized I needed to sort by the second value in the pair instead of the first
    # the searched resource: https://stackoverflow.com/questions/8459231/sort-tuples-based-on-second-parameter
    # additional resource: https://stackoverflow.com/questions/5212870/sorting-a-python-list-by-two-fields
    sort_request = sorted(requests, key=lambda x: (x[1], x[0]))

    do = 0
    pu = 1
    pointer1 = sort_request[do][1] # points to the DO
    pointer2 = sort_request[pu][0] # points to the PU
    print(sort_request) # for testing purposes
    # Now I can access the list with two separate pointers to compare the values
    taxi_number = 1
    # since the pointers are taking the pair index values I also need a move variable
    move = 2
    while move < len(requests):
        print(str(move) + ' taxis required: ' + str(taxi_number))
        print(pointer1, pointer2)
        if pointer1 < pointer2:
            pointer1 = sort_request[do + 1][1]
            pointer2 = sort_request[pu + 1][0]
            move += 1
            do += 1
            pu += 1
        elif pointer1 >= pointer2:
            taxi_number += 1
            pointer2 = sort_request[pu + 1][0]
            move += 1
            pu += 1
    if move == len(requests):
            if pointer1 >= pointer2:
                taxi_number += 1
            return taxi_number
    # return the total number of taxis needed for the request
    print(taxi_number)
    return taxi_number



# print(min_num_taxis([(1,2)]))
# print(min_num_taxis([(1, 4), (2, 9), (3, 6)]))
print(min_num_taxis([(1, 4), (5, 9), (8, 9),(2, 3) ,(8, 9), (10, 12)]))
# print(min_num_taxis([(1, 11), (1, 12), (3, 7), (2, 7), (4, 7), (5, 15), (5, 6), (10, 18), (11, 16), (11, 17), (13,15), (16, 17), (16, 19), (17, 19), (19, 20)]))


