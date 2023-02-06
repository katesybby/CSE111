# Header
'''
Author:
Date:
Purpose:
'''

# pass
x = 9
if x < 10:
    pass    # fills the need for an indented line

# None
x = None    # fills the need for 'something'
if x == None:
    pass

# end
for i in range(10):
    print(i, end=' ')     # prints '0 1 2... 8 9'
    print('X')       # prints '0 1 2... 8 9 X' 

# sep
for i in range(10):
    print(i,i ** 2, sep='-', end=', ')     # prints '0-0, 1-1,... 9-9'

# math
import math
print(math.pi)
print(math.sqrt(138706))

# random module
import random
print(random.randint(1, 100))   # randint
names = ['bob', 'bily', 'bert']   # choice
print(random.choice(names))

# LOOPS
# break statement
for i in range(20):
    if i == 10:
        break
    print(i, end=', ')   # prints '0... 9, '

# continue statement
for i in range(20):
    if i == 10:
        continue
    print(i, end=', ')   # prints '0...9, 11...19' ten is skipped

# using _ as a variable
for _ in range(5):    # replaces i
    print('Hello')

# lower(), upper()
(name.lower())
(name.upper())

# count()
s = 'ergha;skfguhua;dfuvh;'
print(s.count('e'))     # counts the numb of things in string

# split()
(name.split('i'))

# replace()
(name.split('bob', 'luke'))
print(name)  

# is functions
(func.isalpha())
(func.isnumeric())

# lists
print('abc' * 10)
print('-' * 90)     # duplicates '-'
print([0] * 10)     # '0, 0, ...'

# list; names are 4x long
names = ['moby', 'chase', 'bob']
list = []
for name in names:
    if len(name) == 4:
        print


# EXAMPLE
size = int(input('enter size of square: '))
# goal: print 1 - size in decending order creating a box (i.e size = 16 > 4x4 box)
for r in range(1, size + 1):
    # 1 row
    for i in range(r, size ** 2 + 1, size):
        print(i, end=' ')
    print()



# format
def display_hello():
    print('Hello')
display_hello()     # u need this to call the function; first line to run


# purpose of main()
x = 0   # global variable -dont do it
def display_hello():
    print('Hello')
def main():
    display_hello()
main()



# SHOPPING CART PROGRAM
# noun = variable
# verb = function

def display_menu():
    pass
def load():
    pass
def save():
    pass
def add():
    pass
def display_cart(items):
    ''' display items '''
    print('item: ')
    for i in range(len(items)):
        print(f'{items [i]}')

def remove():
    pass
def main():
    items = []
    prices = []

main()
