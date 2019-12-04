# 7kyu on CodeWars: https://www.codewars.com/kata/christmas-baubles-on-the-tree/train/python

# You've came to visit your grandma and she straight away found you a job - her Christmas tree needs decorating!
# She first shows you a tree with an identified number of branches, and then hands you a some baubles (or loads of them!).
# You know your grandma is a very particular person and she would like the baubles to be distributed in the orderly
# manner. You decide the best course of action would be to put the same number of baubles on each of the branches (if
# possible) or add one more bauble to some of the branches - starting from the beginning of the tree.
# In this kata you will return an array of baubles on each of the branches.
# For example:
# 10 baubles, 2 branches: [5,5] 5 baubles, 7 branches: [1,1,1,1,1,0,0] 12 baubles, 5 branches: [3,3,2,2,2]
# The numbers of branches and baubles will be always greater or equal to 0. If there are 0 branches return: "Grandma,
# we will have to buy a Christmas tree first!".
# Good luck - I think your granny may have some minced pies for you if you do a good job!

# It is interesting that these directions did not mention the possibility of floats being entered for testing... so
# I'm adding that into the mix and it took me a while to find where the problem was (in the number of ornaments)
def baubles_on_tree(baubles, branches):
    baubles = int(baubles)
    branches = int(branches)
    # I will start with the conditional of 0 branches
    if branches == 0:
        return 'Grandma, we will have to buy a Christmas tree first!'
    # next I need to make a list out of the baubles and branches
    decorations = []
    number_of_ornaments = baubles/branches
    # if the number is an exact divisor
    if baubles % branches == 0:
        for baubles in range(branches):
            decorations.append(number_of_ornaments)
    # otherwise need to add one to each value until the remainders run out.
    else:
        remainder = baubles % branches
        ornaments_removed = baubles % branches
        for baubles in range(branches):
            while remainder > 0:
                decorations.append(int(number_of_ornaments) + 1)
                remainder -= 1
            decorations.append(int(number_of_ornaments))
    # so this worked but produced too many values in the array. I'm going to delete the extra ones
#             print(ornaments_removed)
        while ornaments_removed > 0:
            decorations.pop()
            ornaments_removed -= 1
    return(decorations)
print baubles_on_tree(2,15)
# I'm sure there is a more concise way to get this result... please feel free to comment with feedback.
