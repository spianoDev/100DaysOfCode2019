# 4kyu on CodeWars: https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
#
# Intervals
# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
#
# Overlapping Intervals
# List containing overlapping intervals:
#
# [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ]
# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
#
# Examples:
# sumIntervals( [
#    [1,2],
#    [6, 10],
#    [11, 15]
# ] ); // => 9
#
# sumIntervals( [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ] ); // => 7
#
# sumIntervals( [
#    [1,5],
#    [10, 20],
#    [1, 6],
#    [16, 19],
#    [5, 11]
# ] ); // => 19

def sum_of_intervals(intervals):
# create a counter
    count = 0
# determine if there is overlap and combine lists that overlap
    intervals_sort = sorted(intervals)
    print(intervals_sort)
    new_intervals = []
    if len(intervals_sort) == 1:
        new_intervals.append(intervals_sort[0])
    if len(intervals_sort) == 2:
        if intervals_sort[0][1] > intervals_sort[1][0]:
            new_intervals.append((intervals_sort[0][0], intervals_sort[1][1]))
        else:
            new_intervals.append(intervals_sort[0])
            new_intervals.append(intervals_sort[1])
    print(new_intervals)
    if len(intervals_sort) > 2:
        pointer1 = 1
        pointer2 = 1
        while intervals_sort[0][pointer1] > intervals_sort[pointer2][0]:
            pointer2 += 1
            print(pointer2)
            break
        new_intervals.append((intervals_sort[0][0], intervals_sort[pointer2-1][1]))
        print(new_intervals)
        while new_intervals[0][1] > intervals_sort[pointer2][0]:
            print('comparisons:')
            print(new_intervals[0][1], intervals_sort[pointer2][0])
            if new_intervals[0][1] > intervals_sort[pointer2][1]:
                print('stop')
                break
            else:
                print('do something')
                new_intervals.pop()
                print(new_intervals)
                new_intervals.append((intervals_sort[0][0], intervals_sort[pointer2][1]))
                print(new_intervals)
                pointer2 += 1
                print('pointer 2 moving up to: ' + str(pointer2))
                if pointer2 == len(intervals_sort):
                    break
        else:
            new_intervals.append(intervals_sort[pointer2])
    print('these are the new intervals: ')
    print(new_intervals)
# count the number of values in each list
    for value in new_intervals:
        print(value)
# since tuples are immutable, I will assign new values to each one
        num1 = value[0]
        num2 = value[1]
        while num1 < num2:
            count += 1
            num1 += 1
        print(count)
    return count
# return the final count (should be the sum of all the intervals)

# sum_of_intervals([(1, 5)]) # 4
# sum_of_intervals([(1, 5), (6, 10)]) # 8
# sum_of_intervals([(1, 5), (1, 5)]) # 4
# sum_of_intervals([(1, 4), (7, 10), (3, 5)]) # 7
# sum_of_intervals([(1,5),(10, 20),(1, 6),(16, 19),(5, 11)]) # 19
sum_of_intervals([(-482, 433), (-344, 441), (-182, 460), (-167, 65), (-135, -93), (-57, 122), (-24, 358), (112, 222), (125, 307), (128, 336), (136, 158), (345, 377), (397, 466), (405, 453)])
# 948
