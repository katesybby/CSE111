# 01 Prove Milestone: Review Python 
# --> 02 Prove: Calling Functions 

"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

import math 

loop = 'y'      # extra feature: looped program

while loop == 'y': 
    w = int(input(f'\nEnter the width of the tire in mm: '))
    a = int(input(f'Enter the aspect ratio of the tire: '))
    d = int(input(f'Enter the diameter of the wheel in inches: '))

    v = math.pi * w * w * a * (w * a + 2540 * d) / 10000000000

    print (f'The approximate volume is {v:.2f} liters')

    # ----
    from datetime import datetime

    current_date_and_time = datetime.now()

    with open("volumes.txt", "at") as volumes_file:

        print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file = volumes_file)
    # ----

    loop = input(f'\nRESTART (y/n)? ')

print (f'\nGoodbye. ')
