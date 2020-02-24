# 6kyu on CodeWars: https://www.codewars.com/kata/57052ac958b58fbede001616/train/python

# Check if given chord is minor or major.
#
# Rules:
#
# Basic minor/major chord have three elements.
#
# Chord is minor when interval between first and second element equals 3 and between second and third -> 4.
#
# Chord is major when interval between first and second element equals 4 and between second and third -> 3.
#
# In minor/major chord interval between first and third element equals... 7.
#
# There is a preloaded list of the 12 notes of a chromatic scale built on C. This means that there are (almost) all allowed note' s names in music.
#
# notes = ['C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'F', ['F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B']
#
# Note that e. g. 'C#' - 'C' = 1, 'C' - 'C#' = 1, 'Db' - 'C' = 1 and 'B' - 'C' = 1.
#
# Input: String of notes separated by whitespace, e. g. 'A C# E'
#
# Output: String message: 'Minor', 'Major' or 'Not a chord'.

# the provided list of chromatic scale notes
notes = ['C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'F', ['F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B']

def minor_or_major(chord):
    chord_notes = chord.split(" ")
    print(chord_notes)
    # first eliminate the 'not a chord options'
    if len(chord_notes) != 3:
        print('Not a chord')
        return 'Not a chord'
    # I need to loop through the notes list to get the three chord index values
    first = 0
    second = 0
    third = 0
    # I discovered I also need index values for the 'flat' notes so I will assign them manually
    for index, tone in enumerate(chord_notes):
        if tone == 'Db':
            chord_notes[index] = 'C#'
        if tone == 'Eb':
            chord_notes[index] = 'D#'
        if tone == 'Gb':
            chord_notes[index] = 'F#'
        if tone == 'Ab':
            chord_notes[index] = 'G#'
        if tone == 'Bb':
            chord_notes[index] = 'A#'
    print(chord_notes)
    for note in notes:
        if note[0] == chord_notes[0]:
            first = notes.index(note)
        if note[0] == chord_notes[1]:
            second = notes.index(note)
        if note[0] == chord_notes[2]:
            third = notes.index(note)
    print(first, second, third)
    # The tricky thing here is if the first number is greater than 5,
    # or the second number is less than the first number, so I will account for that
    # determine if the interval between the first and third notes is 7 half steps
    if first >= 5:
        third += 12
        outer_interval = third - first
        if outer_interval != 7:
            print('Not a chord')
            return 'Not a chord'
    else:
        if third - first != 7:
            print('Not a chord')
            return 'Not a chord'
    if second < first:
        second += 12
    # major chords
    if second - first == 3:
        print('Minor')
        return 'Minor'
    if second - first == 4:
        print('Major')
        return 'Major'
    if second - first != 3 and second - first != 4:
        print('Not a chord')
        return 'Not a chord'

minor_or_major('C D G') # 'Not a chord'
# minor_or_major('C Eb G') # 'Minor'
# minor_or_major('C D E F') # 'Not a chord'
# minor_or_major('A C E') # 'Minor'
# minor_or_major('F A C#') # 'Major'
# minor_or_major('Eb G Bb') # 'Major'

# I thought it would be fun to do a 'musical' Kata after my weekend of music :)
