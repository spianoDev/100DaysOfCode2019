# 8kyu on CodeWars: https://www.codewars.com/kata/holiday-viii-duty-free/train/python

# The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the saving over the normal high street price would effectively cover the cost of your holiday.
#
# You will be given the high street price (normPrice), the duty free discount (discount) and the cost of the holiday.
#
# For example, if a bottle cost 10 normally and the discount in duty free was 10%, you would save 1 per bottle.
# If your holiday cost 500, the answer you should return would be 500.
#
# All inputs will be integers. Please return an integer. Round down.

def duty_free(price, discount, holiday_cost):
    # First I need to determine the discount per bottle
    # Apparently you need one number to be a float in order for the remainder not to get tossed out in python
    discount_amount = float(discount) * price / 100
    print(discount_amount)
    # Next I will need to divide the holiday_cost by that discount_amount and return that number
    # Because I was using a float earlier, now I need to convert the final answer back into an integer
    bottles = holiday_cost / discount_amount
    print(int(bottles))
    return int(bottles)
print duty_free(17, 10, 500)
