# 6kyu on CodeWars: https://www.codewars.com/kata/57091b473f1008c03f001a2a/train/python
#
# Your task is to validate rhythm with a meter.
#
# Rules:
#
# Rhythmic division requires that in one whole note (1) there are two half notes (2) or four quarter notes (4) or eight eighth notes (8).
#
# Examples: 1 = 2 + 2, 1 = 4 + 4 + 4 + 4 ...
# Note that: 2 = 4 + 4, 4 = 8 + 8, 2 = 8 + 8 + 4 ...
# Meter gives an information how many rhythmic types of notes should be in one bar. Bar is the the primary section of a musical score.
#
# Examples:
#        4/4 -> 4 quarter notes in a bar
#        5/2 -> 5 half notes in a bar
#        3/8 -> 3 eighth notes in a bar
# Note that:
# for 4/4 valid bars are: '4444', '88888888', '2488' ...
# for 5/2 valid bars are: '22222', '2244244', '8888244888844' ...
# for 3/8 valid bars are: '888', '48' ...
# Anacrusis occurs when all bars but the first and last are valid, and the notes in the first and last bars when combined would also make a valid bar.
#
# Examples:
# for 4/4 valid anacrusis is -> 44|...|44 or 88|...|888888 or 2|...|488
# for 5/2 valid anacrusis is -> 22|...|222 or 222|...|22 or  2244|...|244
# for 3/8 valid anacrusis is -> 8|...|88 or 4|...|8 or 8|...|4
# Note:
# When anacrusis is valid but other bars in score are not -> return 'Invalid rhythm'
# Input:
#
# meter - array: eg. [4, 4],
# score - string, bars separated with '|': eg. '4444|8484842|888'
#
# Output:
# string message: 'Valid rhythm', 'Valid rhythm with anacrusis' or 'Invalid rhythm'

def validate_rhythm(meter, score):
    print('original meter: ')
    print(meter)
    print('original score: ')
    print(score)
# if the second value of the meter isn't 2, 4, or 8, it isn't valid
    if meter[1] != 1 and meter[1] != 2 and meter[1] != 4 and meter[1] != 8:
        return 'Invalid rhythm'
# separate the bars to compare each chunk of rhythm
    bars = score.split("|")
# need a variable to hold the desired meter
    time_signature = float(meter[0])/float(meter[1])
# need a variable to hold the final total time of each bar
    bar_time = []
# each number technically represents the bottom of a fraction so converting to a decimal that I can add to make a
# whole number will be the easiest mathematical solution
    whole = 1.0/1
    half = 1.0/2
    quarter = 1.0/4
    eighth = 1.0/8
# convert the bar list into the above numerical values
    index = 0
    for bar in bars:
# convert the string numbers into integers so I can use math functions
        rhythm = list(map(int, bar))
        for index, note in enumerate(rhythm):
# change each note value into the decimal variables
            if note == 1:
                rhythm[index] = whole
            if note == 2:
                rhythm[index] = half
            if note == 4:
                rhythm[index] = quarter
            if note == 8:
                rhythm[index] = eighth
# add the values of the notes to bar_time
        print('these are the rhythmic values:')
        print(rhythm)
        bar_value = 0
        for notes in rhythm:
            bar_value += notes
        bar_time.append(bar_value)
    print(bar_time)
# need to make the edge case for anacrusis
    last_index = len(bar_time)-1
    anacrusis = bar_time[0] + bar_time[last_index]
# final comparison of each bar value
    for index, value in enumerate(bar_time):
        print(index, value)
        if value != time_signature:
            if value != time_signature and index != 0 and index != last_index:
                print('Invalid rhythm')
                return 'Invalid rhythm'
            if anacrusis != time_signature:
                print('Invalid rhythm')
                return 'Invalid rhythm'
            if anacrusis == time_signature and index == last_index:
                print('Valid rhythm with anacrusis')
                return 'Valid rhythm with anacrusis'
    print('Valid')
    return 'Valid rhythm'



# validate_rhythm([4, 4], '4444|88888888|22|2488|1') # 'Valid rhythm'
validate_rhythm([3, 8], '888') # 'Valid rhythm'
# validate_rhythm([5, 2], '222|1144|41188|22') # 'Valid rhythm with anacrusis'
# validate_rhythm([4, 4], '44|4444|884884|22|1|44') # 'Valid rhythm with anacrusis'
# validate_rhythm([4, 4], '44|11|224|44') # 'Invalid rhythm'
# validate_rhythm([3, 8], '|884|888|') # 'Invalid rhythm'
# validate_rhythm([4, 4], '44|11|224|44')

