# 6kyu on CodeWars: https://www.codewars.com/kata/who-has-the-most-money/train/python

# You're going on a trip with some students and it's up to you to keep track of how much money each Student has.
# A student is defined like this:
#
# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
# As you can tell, each Student has some fives, tens, and twenties.
# Your job is to return the name of the student with the most money.
# If every student has the same amount, then return "all".
#
# Notes:
#
# Each student will have a unique name
# There will always be a clear winner: either one person has the most, or everyone has the same amount
# If there is only one student, then that student has the most money

# in order to test this locally, I needed to import the student class
class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
# These students were taken from the test examples
phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

def most_money(students):
# first I need to add up all the money each person has
    student_money = []
    for student in students:
        student.total_money = 0
        if student.fives > 0:
            student.total_money += student.fives * 5
        if student.tens > 0:
            student.total_money += student.tens * 10
        if student.twenties > 0:
            student.total_money += student.twenties * 20
        print(student.name + " has $" + str(student.total_money))
        student_money.append(student.total_money)
        # next I need to compare the sums to see who has the most money
    money = sorted(student_money)
    print(money[-1])
#
        # although this is terribly in-efficient, I can loop through the students again to compare values that way
    for student in students:
        total_money = 0
        if student.fives > 0:
            total_money += student.fives * 5
        if student.tens > 0:
            total_money += student.tens * 10
        if student.twenties > 0:
            total_money += student.twenties * 20
        if len(money) == 1:
            print(student.name)
            return student.name
        elif money[0] == money[-1]:
            print('all')
            return 'all'
        elif total_money == money[-1]:
            print(student.name)
            return student.name

most_money([cam, phil, geoff])

