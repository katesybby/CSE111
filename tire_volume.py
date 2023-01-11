# 01 Prove Milestone: Review Python

"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

import math 

width = int(input(f"Enter the width of the tire in mm: "))
aspect_ratio = int(input(f"Enter the aspect ratio of the tire: "))
diameter = int(input(f"Enter the diameter of the wheel in inches: "))


volume = complex(math.pi * width * width * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10,000,000,000)


print (f"The approximate volume is {volume:.2f} liters")