# 02 Checkpoint: Calling Functions 

# the number of manufactured items
# the number of items that the user will pack per box 

import math

items = int(input(f'Enter the number of items: '))
capacity = int(input(f'Enter the number of items per box: '))

box = math.ceil(items / capacity)

print (f'\nFor {items} items, packing {capacity} items in each box, you will need {box} boxes.')