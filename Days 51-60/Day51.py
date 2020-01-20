# 6kyu on CodeWars: https://www.codewars.com/kata/536e9a7973130a06eb000e9f/train/python

# It's a Pokemon battle! Your task is to calculate the damage that a particular move would do using the following formula
# (not the actual one from the game):
#
# damage = 50 * (attack/defense) * effectiveness
# Make sure to round the result up to the nearest integer.
#
# attack = your attack power
# defense = the opponent's defense
# effectiveness = the effectiveness of the attack based on the matchup (see explanation below)
# Effectiveness:
#
# Attacks can be super effective, neutral, or not very effective depending on the matchup.
# For example, water would be super effective against fire, but not very effective against grass.
#
# Super effective: 2x damage
# Neutral: 1x damage
# Not very effective: 0.5x damage
# To prevent this kata from being tedious, you'll only be dealing with four types: fire, water, grass, and electric.
# Here is the effectiveness of each matchup:
#
# fire > grass
# fire < water
# fire = electric
#
# water < grass
# water < electric
#
# grass = electric
#
# For this kata, any type against itself is not very effective.
# Also, assume that the relationships between different types are symmetric
# (if a is super effective against b, then b is not very effective against a).
#
# The function you will create is called calculateDamage, and it takes in your type and the opponent's type as
# strings and the attack and defense as numbers.

import math

def calculate_damage(your_type, opponent_type, attack, defense):
    # since I wasn't passing all the tests I needed to see more of the variables
    print(your_type)
    print(opponent_type)
    print(attack)
    print(defense)
    # I need variables for the different effectiveness outcomes
    if your_type == 'fire' and opponent_type == 'grass' or your_type == 'grass' and opponent_type == 'water':
        effectiveness = 2
    elif your_type == 'water' and opponent_type == 'fire' or your_type == 'electric' and opponent_type == 'water':
        effectiveness = 2
    elif your_type == 'grass' and opponent_type == 'fire' or your_type == 'water' and opponent_type == 'grass':
        effectiveness = .5
    elif your_type == 'fire' and opponent_type == 'water' or your_type == 'water' and opponent_type == 'electric':
        effectiveness = .5
    elif your_type == 'fire' and opponent_type == 'electric' or your_type == 'grass' and opponent_type == 'electric':
        effectiveness = 1
    elif your_type == 'electric' and opponent_type == 'fire' or your_type == 'electric' and opponent_type == 'grass':
        effectiveness = 1
    elif your_type == opponent_type:
        effectiveness = .5
    # First I tested the variables to be sure I was getting the correct answer since I wasn't 100% sure about the task
    damage = 50 * (attack/defense) * effectiveness
    # I re-read the instructions and realized all the numbers needed to be rounded up
    damage = math.ceil(damage)
    damage = int(damage)
    print(damage)
    return damage

print(calculate_damage("water", "water", 120, 130))

