# 5kyu on CodeWars: https://www.codewars.com/kata/5aaae0f5fd8c069e8c00016e/train/python
#
# Given an array of words and a target compound word, your objective is to find the two words which combine into the target word,
# returning both words in the order they appear in the array, and their respective indices in the order they combine to form the
# target word. Words in the array you are given may repeat, but there will only be one unique pair that makes the target compound word.
# If there is no match found, return null/nil/None.
#
# Note: Some arrays will be very long and may include duplicates, so keep an eye on efficiency.
#
# Examples:
#
# fn(['super','bow','bowl','tar','get','book','let'], "superbowl")      =>   ['super','bowl',   [0,2]]
# fn(['bow','crystal','organic','ally','rain','line'], "crystalline")   =>   ['crystal','line', [1,5]]
# fn(['bow','crystal','organic','ally','rain','line'], "rainbow")       =>   ['bow','rain',     [4,0]]
# fn(['bow','crystal','organic','ally','rain','line'], "organically")   =>   ['organic','ally', [2,3]]
# fn(['top','main','tree','ally','fin','line'], "mainline")             =>   ['main','line',    [1,5]]
# fn(['top','main','tree','ally','fin','line'], "treetop")              =>   ['top','tree',     [2,0]]

def compound_match(words, target):
# print for tests in codewars
    print(words)
    print(target)
# variables needed
    count = 0
    count2 = 0
    second_half = []
    first_half = []
    indices = []
# loop through the words
    for word in words:
# loop through the letters of the target word
        while len(word) <= count or word[count] == target[count]:
            if len(word) > count:
                first_half.append(word[count])
                count += 1
                print(count)
            else:
                break
        while len(target) <= count or target[count] == word[count2]:
            if len(target) > count:
                second_half.append(word[count2])
                count += 1
                count2 += 1
            else:
                break
    first_word = ''.join(first_half)
    second_word = ''.join(second_half)
# loop through words again to record the index of each half of the target
    for word in words:
        if word == first_word:
            indices.append(words.index(word))
        if word == second_word:
            indices.append(words.index(word))
    print(first_word, second_word, indices)
    return [first_word, second_word, indices]

# compound_match(['bel', 'bed', 'low', 'grab', 'be', 'knight'], 'bellow') # ['bel','low',[0,2]]
compound_match(['bow','crystal','organic','ally','rain','line'], "rainbow")  # ['bow','rain', [4,0]]
