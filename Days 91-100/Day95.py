# 5kyu on CodeWars: https://www.codewars.com/kata/5340298112fa30e786000688/train/python

# The objective is to return all pairs of integers from a given collection of integers that have a difference of 2.
#
# The result should be sorted in ascending order.
#
# The input will consist of unique values. The order of the integers in the input collection should not matter.
#
# Examples
# [1, 2, 3, 4]      -->  [[1, 3], [2, 4]]
# [4, 1, 2, 3]      -->  [[1, 3], [2, 4]]
# [1, 23, 3, 4, 7]  -->  [[1, 3]]
# [4, 3, 1, 5, 6]   -->  [[1, 3], [3, 5], [4, 6]]

def twos_difference(lst):
# edge case of empty list
    if len(lst) == 0:
        return []
# sort the list
    sort_list = sorted(lst)
    print(sort_list)
# compare each pair of the list
    answer = []
    pointer1 = 1
    pointer2 = 0
    while pointer1 < len(lst):
# if the difference is 2, put the pair as a tuple into an answer list
        if sort_list[pointer1] - sort_list[pointer2] < 2:
            pointer1 += 1
            continue
        if sort_list[pointer1] - sort_list[pointer2] == 2:
            answer.append((sort_list[pointer2], sort_list[pointer1]))
            pointer1 += 1
            pointer2 += 1
            continue
        if sort_list[pointer1] - sort_list[pointer2] > 2:
            pointer2 += 1
            continue
        else:
            break
# return the answer list
    print(answer)
    return answer

# twos_difference([1, 2, 3, 4]) # [(1, 3), (2, 4)]
# twos_difference([1, 3, 4, 6]) # [(1, 3), (4, 6)]
# twos_difference([0, 3, 1, 4]) # [(1, 3)]
# twos_difference([4, 1, 2, 3]) # [(1, 3), (2, 4)]
# twos_difference([6, 3, 4, 1, 5]) # [(1, 3), (3, 5), (4, 6)]
# twos_difference([3, 1, 6, 4]) # [(1, 3), (4, 6)]
# twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]) # [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)]
twos_difference([1, 4, 7, 10]) # []
# twos_difference([]) # []
