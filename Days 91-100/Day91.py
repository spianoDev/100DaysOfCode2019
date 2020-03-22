# 6kyu on CodeWars: https://www.codewars.com/kata/5a516c2efd56cbd7a8000058/train/python

# The number 23 is special in the sense that all of its digits are prime numbers.
# Furthermore, it's a prime itself. There are 4 such numbers between 10 and 100: 23, 37, 53, 73. Let's call these numbers "total primes".
#
# Complete the function that takes a range (a, b) and returns the number of total primes within that range (a <= primes < b).
# The test ranges go up to 107.
#
# Examples
# (10, 100)  ==> 4  # 23, 37, 53, 73
# (500, 600) ==> 3  # 523, 557, 577

# def get_total_primes(a, b):
#     primes = []
#     # first I need a function to record all the prime numbers in the range of a through b
#     for prime in range(a, b):
#        # all prime numbers are greater than 1
#        if prime > 1:
#            for i in range(2, prime):
#                if (prime % i) == 0:
#                    break
#            else:
#                primes.append(prime)
#     # next I need to check the values in primes to see if the digits include non-prime numbers
#     answers = []
#     for number in primes:
#         if '1' not in str(number) and '4' not in str(number) and '6' not in str(number) and '8' not in str(number) and '9' not in str(number) and '0' not in str(number):
#             answers.append(number)
# #     print(answers)
#     # return the length of the answers list
#     return len(answers)
# The above solution works, but times out so below is a refactoring for efficiency

# To cut down on loops inside the larger program, I moved finding the prime numbers
def is_number_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_number_prime(73))

def get_total_primes(a, b):
    primes = []
    # first I need a function to record all the prime numbers in the range of a through b
    for number in range(a, b + 1):
        if is_number_prime(number):
            primes.append(number)

    print(primes)
    # next I need to check the values in primes to see if the digits include non-prime numbers
    answers = []
    for number in primes:
        if '1' not in str(number) and '4' not in str(number) and '6' not in str(number) and '8' not in str(number) and '9' not in str(number) and '0' not in str(number):
            answers.append(number)
    print(answers)
    # return the length of the answers list
    return len(answers)

get_total_primes(10, 100) # 23, 37, 53, 73 => 4
# get_total_primes(500, 600) # 523, 557, 577 => 3

# This solution also works, but times out so I'm out of ideas

