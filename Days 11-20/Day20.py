# 6kyu on CodeWars: https://www.codewars.com/kata/custom-christmas-tree/train/python

# Task
# Christmas is coming, and your task is to build a custom Christmas tree with the specified characters and the specified height.
#
# Inputs:
# chars: the specified characters.
# n: the specified height. A positive integer greater than 2.
# Output:
# A multiline string. Each line is separated by \n. A tree contains two parts: leaves and trunks.
# The leaves should be n rows. The first row fill in 1 char, the second row fill in 3 chars, and so on. A single space will be added between two adjust chars, and some of the necessary spaces will be added to the left side, to keep the shape of the tree. No space need to be added to the right side.
#
# The trunk should be at least 1 unit height, it depends on the value of the n. The minimum value of n is 3, and the height of the tree trunk is 1 unit height. If n increased by 3, and the tree trunk increased by 1 unit. For example, when n is 3,4 or 5, trunk should be 1 row; when n is 6,7 or 8, trunk should be 2 row; and so on.
#
# Still not understand the task? Look at the following example ;-)
#
# Examples
# For chars = "*@o" and n = 3,the output should be:
#
#   *
#  @ o
# * @ o
#   |

 # In looking at this, I can see that the top tier is preceded by 'n' number of spaces. Same with the base value.
 # Also there is a space between each character.

def custom_christmas_tree(chars, n):
    # I want to make sure I don't run out of characters, so I want a list with extra characters inside it
    chars = chars * n
    # I need to split each of the chars elements so I can manipulate them one at a time
    single_char = list(chars)
    print(single_char)
    length = 0
    next_line = ""
    total_lines = n
    answer = []
    result = ''
    # prints the tree with the correct spacing, but the characters are wrong
    while n > 0:
        each_line = (n - 1) * " " + single_char[length] + next_line
        answer.append(each_line)
        answer.append('\n')
        length += 1
        n -= 1
        next_line += " " + single_char[(length + 1)]

    if total_lines == 3:
        answer.append((total_lines - 1) * " " + "|")
    elif total_lines > 3:
        answer.append((total_lines - 1) * " " + "|")
        answer.append('\n')
        answer.append((total_lines - 1) * " " + "|")
    print(result.join(answer))
    return result.join(answer)
#     return '  *\n @ o\n* @ o\n  |'
print custom_christmas_tree("1234",4)

