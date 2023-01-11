# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime as dt

sales_tax = 0.06
discount = 0.10

total = float(input(f"please enter the subtotal: "))

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = dt.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

day_of_week = 1

# alternate option: if day in [2,3]
# 'and' comes b4 'or'
if total >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = total * discount
    print (f"discount amount: {discount:.2f}")
    total -= discount

sales_tax = total * sales_tax
print (f"sales tax amount: {sales_tax:.2f}")

final_total = total + sales_tax

print(f"total: ${final_total:.2f}")
