# 6kyu on CodeWars: https://www.codewars.com/kata/backspaces-in-string/train/python

# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#
# Your task is to process a string with "#" symbols.
#
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    # Because any # later in the string will erase what is already added, I will use a list to store the values
    letters = []
    for char in s:
    # Add all the letters
        if char != '#':
            letters.append(char)
            # remove a letter for each #
        if char == '#' and len(letters) > 0:
            letters.pop()
    answer = ''.join(letters)
    print(answer)
    return answer
print(clean_string('abc####d##c#'))
