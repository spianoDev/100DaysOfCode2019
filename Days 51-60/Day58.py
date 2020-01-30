# 6kyu on CodeWars: https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python

# Let us consider this example (array written in general format):
#
# ls = [0, 1, 3, 6, 10]
#
# Its following parts:
#
# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]
#
# The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.
#
# Other Examples:
# ls = [1, 2, 3, 4, 5, 6]
# parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]
#
# ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
# parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
#
# def parts_sums(ls):
# # variable to store the answer
#     answer = []
# # I need to create a recursive loop that will add all the values
#     while len(ls) >= 1:
# # variable to store sum within each loop
#         sum = 0
# # Add the sum to the answer list
#         for value in ls:
#             sum += value
# # put the sum into the answer list
#         answer.append(sum)
#         print(sum)
# # remove the first value of the list and repeat the loop
#         ls.pop(0)
#         print(ls)
#     if len(ls) == 0:
#         answer.append(0)
# # return the answer list
#     print(answer)
#     return answer
#
# # parts_sums([])
# # => [0]
# # parts_sums([0, 1, 3, 6, 10])
# # => [20, 20, 19, 16, 10, 0]
# parts_sums([1, 2, 3, 4, 5, 6])
# # => [21, 20, 18, 15, 11, 6, 0]

# The above solution works, but isn't efficient enough for the bigger value tests.
# Below is the refactored solution

def parts_sums(ls):
# variable to store the answer
    answer = []
# variable to store sum within each loop
    sum = 0
# Add the sum to the answer list
    for value in ls:
        sum += value
# put the sum into the answer list
    answer.append(sum)
# pointer variable to move on each iteration
    pointer = 0
# loop to iterate through the sums
    while pointer < len(ls):
        sum -= ls[pointer]
        answer.append(sum)
        pointer += 1
#         print(pointer)
    print(answer)
    return answer

parts_sums([])
# => [0]
# parts_sums([0, 1, 3, 6, 10])
# => [20, 20, 19, 16, 10, 0]
# parts_sums([1, 2, 3, 4, 5, 6])
# => [21, 20, 18, 15, 11, 6, 0]
