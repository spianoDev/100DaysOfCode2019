# 5kyu on CodeWars: https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    pig_latin_text = []
# split the text into individual words
    words = text.split(' ')
#     print(words)
# remove the first letter of each word and place that removed letter at the end of each word and add 'ay'
    for word in words:
# filter out the punctuation
        if word.isalpha():
            pig_latin_text.append(word[1:] + word[:1] + 'ay')
        else:
            pig_latin_text.append(word)
# return the list as a new text
#     print(pig_latin_text)
    print(" ".join(pig_latin_text))
    return " ".join(pig_latin_text)


# pig_it('Pig latin is cool') # 'igPay atinlay siay oolcay'
# pig_it('This is my string') # 'hisTay siay ymay tringsay'
pig_it('O tempora o mores !')
