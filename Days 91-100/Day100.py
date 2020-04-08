# 5kyu on CodeWars: https://www.codewars.com/kata/5a3267b2ee1aaead3d000037/train/python

# A 1-800 number is an 11 digit phone number which starts with a 1-800 prefix.

# The remaining 7 digits can be written as a combination of 3 or 4 letter words. e.g.
#
# 1-800-CODE-WAR
# 1-800-NEW-KATA
# 1-800-GOOD-JOB
# The - are included just to improve the readibility.
#
# Story
# A local company has decided they want to reserve a 1-800 number to help with advertising.
#
# They have already chosen what words they want to use, but they are worried that maybe that same phone number could spell out other words as well. Maybe bad words. Maybe embarrassing words.
#
# They need somebody to check for them so they can avoid any accidental PR scandals!
#
# That's where you come in...
#
# Kata Task
# There is a preloaded array of lots of 3 and 4 letter (upper-case) "words".
#
# For Python it is: WORDS
# Given the 1-800 (phone word) number that the company wants to use, you need to check against all known words and return the set of all possible 1-800 numbers which can be formed using those same digits.
#
# Notes
# The desired phone-word number provided by the company is formatted properly. No need to check.
# All the letters are upper-case. No need to check.
# Only words in the list are allowed.

# provided list of words:
WORDS = ['ACT', 'ADD', 'ALL', 'APE', 'AND', 'ANN', 'ANY', 'ANT', 'ARE', 'ART', 'ASS',
    'BAD', 'BAR', 'BAT', 'BAY', 'BEE', 'BIG', 'BIT', 'BOB', 'BOY', 'BUN', 'BUT',
    'CAN', 'CAR', 'CAT', 'COT', 'COW', 'CUT',
    'DAD', 'DAY', 'DEW', 'DID', 'DIN', 'DOG', 'DON', 'DOT', 'DUD',
    'EAR', 'EAT', 'EEL', 'EGG', 'ERR', 'EYE',
    'FAG', 'FAR', 'FLY', 'FOR', 'FUN', 'FUR',
    'GAY', 'GET', 'GOT', 'GUM', 'GUN', 'GUY', 'GUT', 'GYM',
    'HAS', 'HAT', 'HER', 'HEY', 'HIM', 'HIS', 'HIT', 'HOW', 'HUG', 'HUN',
    'ICE', 'INK', 'ITS', 'IVE',
    'JAN', 'JET', 'JOB', 'JOT', 'JOY',
    'KEY',
    'LAP', 'LAY', 'LIE', 'LET', 'LOG',
    'MAN', 'MAP', 'MAY', 'MEN', 'MOM', 'MUD', 'MUM',
    'NAP', 'NEW', 'NOD', 'NOT', 'NOW',
    'OAR', 'ODD', 'OFF', 'OLD', 'ONE', 'OUR', 'OUT',
    'PAN', 'PAL', 'PAT', 'PAW', 'PEN', 'PET', 'PIG', 'PIT', 'POT', 'PRO', 'PUT',
    'QUO',
    'RAG', 'RAM', 'RAN', 'RAP', 'RAT', 'RED', 'RIP', 'ROD', 'ROT', 'RUN', 'RUT',
    'SAT', 'SAW', 'SAY', 'SEA', 'SEE', 'SEX', 'SHE', 'SOY', 'SUN', 'SUX',
    'TAN', 'TAT', 'TEA', 'THE', 'TIN', 'TIP', 'TIT', 'TON', 'TOP', 'TOO', 'TWO',
    'URN', 'USE',
    'VAN', 'VET', 'VIP',
    'WAR', 'WAS', 'WAY', 'WED', 'WHO', 'WHY', 'WIN', 'WON',
    'XXX',
    'YAK', 'YAM', 'YAP', 'YOU', 'YUM',
    'ZAP', 'ZIP', 'ZIT', 'ZOO',
    'ABLE', 'ACED', 'AGOG', 'AHEM', 'AHOY', 'ALLY', 'AMEN', 'ANTI', 'ANTS', 'ANUS', 'APES', 'ARMY', 'ARSE', 'ARTY', 'AVID', 'AWED',
    'BABY', 'BARS', 'BATS', 'BAYS', 'BEAR', 'BEES', 'BILL', 'BITE', 'BITS', 'BLOW', 'BLUE', 'BOLD', 'BONE', 'BOOB', 'BOOM', 'BOSS', 'BOYS', 'BUFF', 'BUNG', 'BUNS', 'BUMS', 'BURP', 'BUST', 'BUSY', 'BUZZ',
    'CANS', 'CANT', 'CARS', 'CART', 'CATS', 'CHAP', 'CHIC', 'CHUM', 'CIAO', 'CLAP', 'COCK', 'CODE', 'COOL', 'COWS', 'COZY', 'CRAB', 'CREW', 'CURE', 'CULT',
    'DADS', 'DAFT', 'DAWN', 'DAYS', 'DECK', 'DEED', 'DICK', 'DING', 'DOGS', 'DOTS', 'DOLL', 'DOLT', 'DONG', 'DOPE', 'DOWN', 'DRAW', 'DUCK', 'DUDE', 'DUMB', 'DUTY',
    'EARL', 'EARN', 'EARS', 'EASY', 'EATS', 'EDGE', 'EELS', 'EGGS', 'ENVY', 'EPIC', 'EYES',
    'FACE', 'FAGS', 'FANG', 'FARM', 'FART', 'FANS', 'FAST', 'FEAT', 'FEET', 'FISH', 'FIVE', 'FIZZ', 'FLAG', 'FLEW', 'FLIP', 'FLOW', 'FOOD', 'FORT', 'FUCK', 'FUND',
    'GAIN', 'GEEK', 'GEMS', 'GIFT', 'GIRL', 'GIST', 'GIVE', 'GLEE', 'GLOW', 'GOLD', 'GOOD', 'GOSH', 'GRAB', 'GRIN', 'GRIT', 'GROT', 'GROW', 'GRUB', 'GUNS', 'GUSH', 'GYMS',
    'HAIL', 'HAIR', 'HALO', 'HANG', 'HATS', 'HEAD', 'HEAL', 'HEIR', 'HELL', 'HELP', 'HERE', 'HERO', 'HERS', 'HIGH', 'HIRE', 'HITS', 'HOLY', 'HOPE', 'HOST', 'HUNK', 'HUGE', 'HUNG', 'HUNS', 'HURT',
    'ICON', 'IDEA', 'IDLE', 'IDOL', 'IOTA',
    'JAZZ', 'JERK', 'JESS', 'JETS', 'JINX', 'JOBS', 'JOHN', 'JOKE', 'JUMP', 'JUNE', 'JULY', 'JUNK', 'JUST',
    'KATA', 'KEYS', 'KICK', 'KIND', 'KING', 'KISS', 'KONG', 'KNOB', 'KNOW',
    'LARK', 'LATE', 'LEAN', 'LICE', 'LICK', 'LIKE', 'LION', 'LIVE', 'LOGS', 'LOCK', 'LONG', 'LOOK', 'LORD', 'LOVE', 'LUCK', 'LUSH',
    'MAKE', 'MANY', 'MART', 'MATE', 'MAXI', 'MEEK', 'MIKE', 'MILD', 'MINT', 'MMMM', 'MOMS', 'MOOD', 'MOON', 'MOOT', 'MUCH', 'MUFF', 'MUMS', 'MUTT',
    'NAPS', 'NAZI', 'NEAT', 'NECK', 'NEED', 'NEWS', 'NEXT', 'NICE', 'NICK', 'NOON', 'NOSE', 'NOTE',
    'OARS', 'OATS', 'ONCE', 'ONLY', 'OPEN', 'ORGY', 'OVAL', 'OVER',
    'PANS', 'PALS', 'PART', 'PAST', 'PATS', 'PAWS', 'PEAR', 'PERT', 'PENS', 'PETS', 'PHEW', 'PIPE', 'PIPS', 'PLAN', 'PLUM', 'PLUS', 'POET', 'POOF', 'POOP', 'POSH', 'POTS', 'PROS', 'PSST', 'PUKE', 'PUNK', 'PURE', 'PUSH', 'PUSS',
    'QUAD', 'QUAK', 'QUID', 'QUIT',
    'RANT', 'RAPE', 'RAPS', 'RAPT', 'RATE', 'RAMS', 'RATS', 'REAP', 'RICK', 'RING', 'RIPE', 'ROOT', 'ROSE', 'ROSY', 'ROTS', 'RUNT', 'RUTS',
    'SAFE', 'SAGE', 'SANE', 'SAVE', 'SAWS', 'SEEK', 'SEXY', 'SHAG', 'SHIT', 'SICK', 'SIGH', 'SIRE', 'SLAG', 'SLIT', 'SLUT', 'SNAP', 'SNOG', 'SNUG', 'SOFT', 'SOON', 'SOUL', 'SOUP', 'SPRY', 'STIR', 'STUN', 'SUCK', 'SWAG', 'SWAY',
    'TACT', 'TANK', 'TANS', 'THAT', 'THIS', 'TIME', 'TINS', 'TINY', 'TITS', 'TOES', 'TONS', 'TONY', 'TOPS', 'TOYS',
    'UBER', 'URNS', 'USED', 'USER', 'USES',
    'VAIN', 'VAMP', 'VARY', 'VEIN', 'VENT', 'VERY', 'VEST', 'VIEW', 'VIVA', 'VOLT', 'VOTE',
    'WAFT', 'WAGE', 'WAKE', 'WALK', 'WALL', 'WANG', 'WANK', 'WANT', 'WARD', 'WARM', 'WARP', 'WARS', 'WART', 'WASH', 'WAVE', 'WEAR', 'WEDS', 'WEED', 'WEEN', 'WELD', 'WHAT', 'WHEE', 'WHEW', 'WHIP', 'WHIZ', 'WHOA', 'WIFE', 'WILL', 'WIND', 'WING', 'WINK', 'WINS', 'WIRE', 'WISH', 'WITH', 'WORD', 'WORK', 'WRAP',
    'XMAN', 'XMEN', 'XRAY', 'XTRA', 'XXXX',
    'YANK', 'YAKS', 'YAMS', 'YAPS', 'YARD', 'YARN', 'YELP', 'YERN', 'YOKE', 'YOLK', 'YULE',
    'ZANY', 'ZAPS', 'ZIPS', 'ZITS', 'ZERO', 'ZOOM', 'ZOOS']

def check1800(s):
# variable to hold the other 800 options
    other_800s = []
    letters_in_s = []
    first_word = []
    second_word = []
# split the characters in the given number to focus only on the alpha characters
    for char in s:
        if char.isalpha():
            letters_in_s.append(char)
    print(letters_in_s)
# variables to group letters together according to the number on the phone
    phone_numbers = {
    'twos': ['A', 'B', 'C'],
    'threes': ['D', 'E', 'F'],
    'fours': ['G', 'H', 'I'],
    'fives': ['J', 'K', 'L'],
    'sixes': ['M', 'N', 'O'],
    'sevens': ['P', 'Q', 'R', 'S'],
    'eights': ['T', 'U', 'V'],
    'nines': ['W', 'X', 'Y', 'Z']
    }
# check the letters in letters_in_s against the possible phone_numbers
    first_letter = []
    second_letter = []
    third_letter = []
#     middle_letter = []
    last_letter = []
    penultimate_letter = []
    third_from_end_letter = []
    for letter in phone_numbers['twos']:
        if letters_in_s[0] == letter:
            first_letter.append(phone_numbers['twos'])
        if letters_in_s[1] == letter:
            second_letter.append(phone_numbers['twos'])
        if letters_in_s[2] == letter:
            third_letter.append(phone_numbers['twos'])
        if letters_in_s[-1] == letter:
            last_letter.append(phone_numbers['twos'])
        if letters_in_s[-2] == letter:
            penultimate_letter.append(phone_numbers['twos'])
        if letters_in_s[-3] == letter:
            third_from_end_letter.append(phone_numbers['twos'])
    for letter in phone_numbers['threes']:
        if letters_in_s[0] == letter:
            first_letter.append(phone_numbers['threes'])
        if letters_in_s[1] == letter:
           second_letter.append(phone_numbers['threes'])
        if letters_in_s[2] == letter:
           third_letter.append(phone_numbers['threes'])
        if letters_in_s[-1] == letter:
           last_letter.append(phone_numbers['threes'])
        if letters_in_s[-2] == letter:
           penultimate_letter.append(phone_numbers['threes'])
        if letters_in_s[-3] == letter:
           third_from_end_letter.append(phone_numbers['threes'])
    for letter in phone_numbers['fours']:
        if letters_in_s[0] == letter:
           first_letter.append(phone_numbers['fours'])
        if letters_in_s[1] == letter:
           second_letter.append(phone_numbers['fours'])
        if letters_in_s[2] == letter:
           third_letter.append(phone_numbers['fours'])
        if letters_in_s[-1] == letter:
           last_letter.append(phone_numbers['fours'])
        if letters_in_s[-2] == letter:
           penultimate_letter.append(phone_numbers['fours'])
        if letters_in_s[-3] == letter:
           third_from_end_letter.append(phone_numbers['fours'])
    for letter in phone_numbers['fives']:
        if letters_in_s[0] == letter:
           first_letter.append(phone_numbers['fives'])
        if letters_in_s[1] == letter:
           second_letter.append(phone_numbers['fives'])
        if letters_in_s[2] == letter:
           third_letter.append(phone_numbers['fives'])
        if letters_in_s[-1] == letter:
           last_letter.append(phone_numbers['fives'])
        if letters_in_s[-2] == letter:
           penultimate_letter.append(phone_numbers['fives'])
        if letters_in_s[-3] == letter:
           third_from_end_letter.append(phone_numbers['fives'])
    for letter in phone_numbers['sixes']:
        if letters_in_s[0] == letter:
           first_letter.append(phone_numbers['sixes'])
        if letters_in_s[1] == letter:
           second_letter.append(phone_numbers['sixes'])
        if letters_in_s[2] == letter:
           third_letter.append(phone_numbers['sixes'])
        if letters_in_s[-1] == letter:
           last_letter.append(phone_numbers['sixes'])
        if letters_in_s[-2] == letter:
           penultimate_letter.append(phone_numbers['sixes'])
        if letters_in_s[-3] == letter:
           third_from_end_letter.append(phone_numbers['sixes'])
    for letter in phone_numbers['sevens']:
        if letters_in_s[0] == letter:
           first_letter.append(phone_numbers['sevens'])
        if letters_in_s[1] == letter:
           second_letter.append(phone_numbers['sevens'])
        if letters_in_s[2] == letter:
           third_letter.append(phone_numbers['sevens'])
        if letters_in_s[-1] == letter:
           last_letter.append(phone_numbers['sevens'])
        if letters_in_s[-2] == letter:
           penultimate_letter.append(phone_numbers['sevens'])
        if letters_in_s[-3] == letter:
           third_from_end_letter.append(phone_numbers['sevens'])
    for letter in phone_numbers['eights']:
        if letters_in_s[0] == letter:
           first_letter.append(phone_numbers['eights'])
        if letters_in_s[1] == letter:
           second_letter.append(phone_numbers['eights'])
        if letters_in_s[2] == letter:
           third_letter.append(phone_numbers['eights'])
        if letters_in_s[-1] == letter:
           last_letter.append(phone_numbers['eights'])
        if letters_in_s[-2] == letter:
           penultimate_letter.append(phone_numbers['eights'])
        if letters_in_s[-3] == letter:
           third_from_end_letter.append(phone_numbers['eights'])
    for letter in phone_numbers['nines']:
        if letters_in_s[0] == letter:
           first_letter.append(phone_numbers['nines'])
        if letters_in_s[1] == letter:
           second_letter.append(phone_numbers['nines'])
        if letters_in_s[2] == letter:
           third_letter.append(phone_numbers['nines'])
        if letters_in_s[-1] == letter:
           last_letter.append(phone_numbers['nines'])
        if letters_in_s[-2] == letter:
           penultimate_letter.append(phone_numbers['nines'])
        if letters_in_s[-3] == letter:
           third_from_end_letter.append(phone_numbers['nines'])
    print(first_letter[0][0], second_letter)

    first_two_matches = []
    first_three_matches = []
    second_two_matches = []
    last_three_matches = []
# check the WORDS list against the first three letters of letters_in_s for a list of first words
    for word in WORDS:
        if word[0] == first_letter[0][0] or word[0] == first_letter[0][1] or word[0] == first_letter[0][2]:
            first_word.append(word)
    print(first_word)
    for word in first_word:
        if word[1] == second_letter[0][0] or word[1] == second_letter[0][1] or word[1] == second_letter[0][2]:
            first_two_matches.append(word)
    print(first_two_matches)
    for word in first_two_matches:
        if word[2] == third_letter[0][0] or word[2] == third_letter[0][1] or word[2] == third_letter[0][2]:
            first_three_matches.append(word)
    print(first_three_matches)
# check the WORDS list against the last three letters of letters_in_s for a list of second words

    for word in WORDS:
        if word[-1] == last_letter[0][0] or word[-1] == last_letter[0][1] or word[-1] == last_letter[0][2]:
            second_word.append(word)
    print(second_word)
    for word in second_word:
        if word[-2] == penultimate_letter[0][0] or word[-2] == penultimate_letter[0][1] or word[2] == penultimate_letter[0][2]:
            second_two_matches.append(word)
    print(second_two_matches)
    for word in second_two_matches:
        if word[-3] == third_from_end_letter[0][0] or word[-3] == third_from_end_letter[0][1] or word[-3] == third_from_end_letter[0][2]:
            last_three_matches.append(word)
    print(last_three_matches)

#         if word[-1] == letters_in_s[-1] and word[-2] == letters_in_s[-2] and word[-3] == letters_in_s[-3]:
#             second_word.append(word)
#     print(first_two_matches)
#     print(second_word)
check1800('1-800-CODE-WAR') # ["1-800-CODE-WAR", "1-800-CODE-YAP", "1-800-CODE-WAS", "1-800-CODE-ZAP"]
