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

def sorted_requests(value):
    return value[0]

def min_num_taxis(requests):
    # After some failed tests, I am going to try to sort the values but I need a new function to do that
    request_sort = requests.sort(key = sorted_requests)
    sorted(requests)
#     print(request_sort)
    print(requests)

    taxi_number = 1
    # In order to make a comparison between entries, I will make a new array with all the values
    requestArray = []
    # Unless empty, 1 taxi will always be required
    for request in requests:
        requestArray.append(request)
        print(request)

#         Compare the first number (PO) of the second pair to the second number (DO) of the first pair.
        if len(requestArray) > 1:
            # Access the first number (PO) of each pair (I can do this by index number)
             #If the DO is less than or equal to the PO increment the number of taxis needed by 1
            if request[0] < requestArray[0][1]:
                print('yes')
                taxi_number += 1

        #If many pairs, compare these numbers to determine if more taxis are needed
    # return the total number of taxis needed for the request
    print(taxi_number)
    return taxi_number




print(min_num_taxis([(1, 11), (1, 12), (3, 7), (3, 7), (4, 7), (5, 15), (5, 6), (10, 18), (11, 16), (11, 17), (13, 15), (16, 17), (16, 19), (17, 19), (19, 20)]))


