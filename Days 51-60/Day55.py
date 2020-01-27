# 6kyu on CodeWars: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    print(a, b)
    # This would be a great challenge to use a pointer to avoid quadratic time complexity
    # first eliminate edge case of empty b = []
    if b == []:
        print(a)
        return a
    # because I'm removing an element, I need to start from the end of the list
    pointer = len(a)-1
    # Use a recursive loop to cycle through all the values of 'a' if 'b' only has one value
    if len(b) == 1:
        while pointer >= 0:
            if b[0] != a[pointer]:
                pointer -= 1
            if b[0] == a[pointer]:
                a.remove(a[pointer])
                pointer -= 2
        print(a)
        return a
    # if 'b' has more than one item I need a second pointer this will be easier with sorted lists
    # again start with edge case:
    if a == []:
        return a
    sort_a = sorted(a)
    sort_b = sorted(b)
    print(sort_a)
    print(sort_b)
    # I still want to work from the back of the lists
    pointer_a = len(a)-1
    pointer_b = len(b)-1
#     again I want a recursive loop to cycle through all the values, but now I need a new conditional

    while pointer_b > 0 and pointer_a > 0:
    # if the values are equal, delete the value from 'a', move both pointers
        if sort_a[pointer_a] == sort_b[pointer_b]:
            sort_a.remove(sort_a[pointer_a])
    # if the value of 'a' is smaller than 'b' move pointer_b
        if sort_a[pointer_a] < sort_b[pointer_b]:
            pointer_b -= 1
    # if the value of 'a' is larger than 'b' move pointer_a
        if sort_a[pointer_a] > sort_b[pointer_b]:
            pointer_a -= 1

    print(sort_a)
    return sort_a

# array_diff([1, 2, 2], [1])
# => [2,2]
# array_diff([3, 14, 3, 19, -20, 19, 10, 1, -1, -8, -20, 17, 10, 0, 18, 8], [7, -18, 0, -10, 7, 6, -16, -9, -4, 10,-17, 14, 5, 12, -6, 1, -7])
# => [3, 3, 19, -20, 19, -1, -8, -20, 17, 18, 8]
# array_diff([], [1,2])
# => []
# array_diff([-1, 8, 2, 16, -4, -14, -16, 19, 19, 8, 8, 10, -19],  [5, 4, -7, -11, 15, 1, -20, -18, 10, 18, -10, 2, -1, -2, -5, 1, 6, -20, -7])
array_diff([7, 20, 0, 7, 8, 2, -17], [2, -8, 16, 10, 15, -9, -17, 19, -9, -14, 10, 20, -20, -6, -19, -17, -14, -3])
# array_diff([1,2], [2,3,4,5])

# I was able to pass all the given tests, but each new condition of the random test meant refactoring the code so I
# am going to stop where the code is for now.
