# 6kyu on CodeWars: https://www.codewars.com/kata/5800b6568f7ddad2c10000ae/train/python

# Given a positive integer as input, return the output as a string in the following format:

#   Each element, corresponding to a digit of the number, multiplied by a power of 10 in such a way
#   that with the sum of these elements you can obtain the original number.
#
#   Examples
#   Input	Output
#   0	""
#   56	"5*10+6"
#   60	"6*10"
#   999	"9*100+9*10+9"
#   10004	"1*10000+4"


# def simplify(number):
#     number_list = []
#     answer = []
# # make the number into a string and put into a list
#     for digit in str(number):
#         number_list.append(digit)
# # working from the back of the list, add the digit to answer list
#     pointer = -1
#     power_of_ten = 10
#     while abs(pointer) <= len(number_list):
#         if int(number_list[pointer]) != 0 and pointer == -1:
#             answer.insert(0, number_list[pointer])
#             pointer -= 1
# # add the + character and the next digit multiplied by the unit value unless the digit is zero
#         else:
#             if pointer < -1 and int(number_list[pointer]) != 0:
#                 answer.insert(0, '+')
#                 answer.insert(0, str(power_of_ten))
#                 power_of_ten *= power_of_ten
#                 answer.insert(0, '*')
#                 answer.insert(0, number_list[pointer])
#                 pointer -= 1
#             elif pointer < -1 and int(number_list[pointer]) == 0:
#                 power_of_ten *= power_of_ten
#                 pointer -= 1
# # join the answer list and return it as a string
#     print("".join(answer))
#     return ''.join(answer)

# The above code works, but times out.
# try refactoring to use division and multiply by the number of digits in the number

def simplify(number):
    print(number)
# create necessary variables
    answer = []
    string_number = str(number)
    num_digits = len(string_number)
    index = 0
# using the num_digits, determine the formula
    while num_digits > 0 and index < len(string_number):
        if string_number[index] != '0' and index < len(string_number)-1:
            answer.append(string_number[index]+'*'+str(10**num_digits//10))
            index += 1
            num_digits -= 1
        else:
            index += 1
            num_digits -= 1
    if string_number[-1] != '0':
        answer.append(string_number[-1])

    print('+'.join(answer))
    return '+'.join(answer)



simplify(8964631) # "8*1000000+9*100000+6*10000+4*1000+6*100+3*10+1"
# simplify(56) #"5*10+6"
# simplify(999) #"9*100+9*10+9"
# simplify(11) # "1*10+1"
# simplify(991) # "9*100+9*10+1"
# simplify(47) # "4*10+7"
# simplify(234) # "2*100+3*10+4"
# simplify(196587) # "1*100000+9*10000+6*1000+5*100+8*10+7"
# simplify(660)
