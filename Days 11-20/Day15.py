# 8kyu on CodeWars: https://www.codewars.com/kata/sleigh-authentication/train/python

# Christmas is coming and many people dreamed of having a ride with Santa's sleigh. But, of course, only Santa himself
# is allowed to use this wonderful transportation. And in order to make sure, that only he can board the sleigh,
# there's an authentication mechanism.

# Your task is to implement the authenticate() method of the sleigh, which takes the name of the person, who wants to
# board the sleigh and a secret password. If, and only if, the name equals "Santa Claus" and the password is "Ho Ho
# Ho!" (yes, even Santa has a secret password with uppercase and lowercase letters and special characters :D), the
# return value must be true. Otherwise it should return false.

# Examples:

# sleigh = Sleigh()
# sleigh.authenticate('Santa Claus', 'Ho Ho Ho!') # must return True
#
# sleigh.authenticate('Santa', 'Ho Ho Ho!') # must return False
# sleigh.authenticate('Santa Claus', 'Ho Ho!') # must return False
# sleigh.authenticate('jhoffner', 'CodeWars') # Nope, even Jake is not allowed to use the sleigh ;)

# I'm running out of holiday themed Kata, so I went back to a level 8
class Sleigh(object):
    def authenticate(self, name, password):
    # using self. will declare the specific instance of the authentication
        self.name = name
        self.password = password
        if self.name == 'Santa Claus' and self.password == 'Ho Ho Ho!':
            return True
        else:
            return False

sleigh = Sleigh()
print sleigh.authenticate('Santa Claus', 'Ho Ho Ho!')

