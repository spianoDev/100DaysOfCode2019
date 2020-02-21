# 5kyu on CodeWars: https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

# Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
#
# apples, pears
# grapes
# bananas
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"
def solution(string, markers):
    print('original string: ')
    print(string)
    print('original markers: ')
    print(markers)
    # I need to search the string for each of the provided markers
#     for index, char in enumerate(string):
#         print(index, char) # interestingly the '\n' is a single char
    for char in string:
        if char == markers[0]:
            mark_index = string.find(markers[0])
#             print(mark_index) # This is where the marker is
            new_line_index = string.find('\n')
            print(new_line_index) # This is where the new line is
    # remove the markers and all text after the marker until '\n' (new line)
    # and trim the whitespace at the end of each line
            new_string = string[0:mark_index:].strip() + string[new_line_index::]
            next_section = string[new_line_index + 1::]
            print(new_string)
#             string = new_string
        elif char == markers[1]:
            mark_index = new_string.find(markers[1])
            next_line_index = next_section.find('\n', 1)
            print(next_line_index)
            final_string = new_string[0:mark_index:].strip()
            print(final_string)

            return final_string


# solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) # "apples, pears\ngrapes\nbananas"
solution("a #b\nc\nd $e f g", ["#", "$"]) # "a\nc\nd"
