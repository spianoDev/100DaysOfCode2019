# 6kyu on CodeWars: https://www.codewars.com/kata/53e895e28f9e66a56900011a/train/python

# Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text.
# This count excludes numbers, spaces and all punctuation marks.
# Upper and lower case versions of a character are equivalent and the result should all be in lowercase.

# The function should return a list of tuples (in Python and Haskell) or arrays (in other languages) sorted by the most frequent letters first.
# The Rust implementation should return an ordered BTreeMap.
# Letters with the same frequency are ordered alphabetically.

# For example:
# letter_frequency('aaAabb dddDD hhcc')
#  => [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]

#  Letter frequency analysis is often used to analyse simple substitution cipher texts like those created by the Caesar cipher.

def letter_frequency(text):
    print(text)
  # I'm going to keep my time complexity down by using a frequency counter
    frequency_tup = ()
    answer = []
    #convert all the text to lowercase
    text = text.lower()
    for char in text:
    # first I want to find only the alpha characters
        if char.isalpha():
        # now I want to count the frequency and convert to lower case
            frequency_tup = (char, text.count(char))
            answer.append(frequency_tup)
        # I'm returning the correct count, but every character has an entry including repeats
        # So, I am going to sort the responses by most frequent and eliminate repeats.
    sort_frequency = sorted(answer, key=lambda x: x[1])
    print(sort_frequency)
    # finally, I will eliminate the extra values
    # after some experimentation, I found this resource: https://www.w3schools.com/python/showpython.asp?filename=demo_howto_remove_duplicates2
    def my_function(x):
      return list(dict.fromkeys(x))

    removed_duplicates = my_function(sort_frequency)
    print(removed_duplicates)
    # finally return the list sorted by largest frequency first (the negative meaning reverse order), then alpha order
    largest_frequency = sorted(removed_duplicates, key=lambda x: (-x[1], x[0]))

    print(largest_frequency)
    return largest_frequency
# letter_frequency('h1Yes234  Holy')
# letter_frequency('hello')
# => [('l', 2), ('e', 1), ('h', 1), ('o', 1)]
# letter_frequency('wklv lv d vhfuhw phvvdjh')
# => [('v', 5), ('h', 4), ('d', 2), ('l', 2), ('w', 2), ('f', 1), ('j', 1), ('k', 1), ('p', 1), ('u', 1)]
letter_frequency("As long as I'm learning something, I figure I'm OK - it's a decent day.")
# => [('i', 7), ('a', 5), ('e', 5), ('n', 5), ('g', 4), ('s', 4), ('m', 3), ('o', 3), ('t', 3), ('d', 2), ('l', 2), ('r', 2), ('c', 1), ('f', 1), ('h', 1), ('k', 1), ('u', 1), ('y', 1)]
# letter_frequency('IWT LDGAS XH HIXAA P LTXGS EAPRT, STHEXIT BN TUUDGIH ID BPZT RATPG PCS ETGUTRI HTCHT DU XI.')
# => [('t', 12), ('i', 7), ('h', 6), ('a', 5), ('g', 5), ('p', 5), ('x', 5), ('d', 4), ('s', 4), ('u', 4), ('e', 3), ('r', 3), ('b', 2), ('c', 2), ('l', 2), ('n', 1), ('w', 1), ('z', 1)]
