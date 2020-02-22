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
    # I need an edge case of an empty marker list
    if len(markers) == 0:
        return string
    print('original string: ')
    print(string)
    print('original markers: ')
    print(markers)
    # I need to make the string variables global so I can access them outside of their functions
    new_string = ''
    final_string = ''
    answer_string = ''
    next_section = ''
    # I also need to make sure the order of the markers is always dealing with them in order
    if string.find(markers[1]) < string.find(markers[0]):
        placeholder = markers[0]
        markers[0] = markers[1]
        markers[1] = placeholder
    # I need to search the string for each of the provided markers
#     for index, char in enumerate(string):
#         print(index, char) # interestingly the '\n' is a single char
    for char in string:
        if char == markers[0]:
            mark_index = string.find(markers[0])
            print(mark_index) # This is where the marker is
            new_line_index = string.find('\n')
#             print(new_line_index) # This is where the new line is
    # remove the markers and all text after the marker until '\n' (new line)
    # and trim the whitespace at the end of each line
            new_string = string[0:mark_index:].strip() + string[new_line_index::]
            next_section = string[new_line_index + 1::]
            print(new_string)
    # if the marker exists after the first '\n'
            next_line_index = next_section.find('\n', 1)
            if mark_index > next_line_index:
                answer_string = new_string[0:mark_index:].strip()
                print(answer_string)
    # if a second marker exists after the first '\n'
            next_mark_index = new_string.find(markers[0], 1)
            print('the next mark index ')
            print(next_mark_index)
    # if there is a second marker that exists after the first '\n'
        elif char == markers[1]:
            mark_index = new_string.find(markers[1])
            next_line_index = next_section.find('\n', 1)
#             print(next_line_index)
    # I had to subtract 1 from the index because of the elimination of the space in previous line
            final_string = new_string[0:mark_index - 1:].strip()
            print(final_string)
    # need conditional if there is no second marker
    print(len(final_string))
    print(len(new_string))
    if len(final_string) == 0:
        print('This is the answer: ' + answer_string)
        return answer_string
    elif len(final_string) != 0:
        print('This is the answer: ' + final_string)
        return final_string
    print('This is the answer: ' + new_string)
    return new_string

# solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) # "apples, pears\ngrapes\nbananas"
# solution("a #b\nc\nd $e f g", ["#", "$"]) # "a\nc\nd"
# below solution doesn't have the second marker and right now returns nothing
# solution("apples, pears # and bananas \ngrapes \navocado @apples", ['@', '!']) # 'apples, pears # and bananas\ngrapes\navocado'
# below solution has the first marker twice
# solution("apples, pears # and bananas \ngrapes \nbananas #!apples", ['#', '!']) # 'apples, pears\ngrapes\nbananas'
solution('apples, pears 1 and bananas \ngrapes \navocado *apples', ['*', '1']) # 'apples, pears\ngrapes\navocado'

# I will come back to this one, but the tests scale out as I solve each problem which is annoying. If the directions
# had been more clear or the attempts provide more feedback, I would have approached this problem very differently.
