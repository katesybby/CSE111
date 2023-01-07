# NOTES ON CODING STYLE REQ'S

# variables: all lowercase, no abreviations
first_name = 'Bob'

# int, float, str and boolean
age = 45
gpa = 3,345
name = 'Bob'
happy = True

# the type() function
age = int(input('Enter Age: '))
print(type(age))  #displays int/float/str
print(age + 10)

# shorthand operators
x = 9
x = x + 1
x += 1
x /= 1 
x *= 1
x -= 1
x //= 1     # whole numb when divided (int)
x %= 1      # remainder when divided (int)

# formated string
x = 9
y = 10
print(f'x = {x}, y = {y}')

x = 9.398045
y = 10.3482765
print(f'x = {x:.3f}, y = {y:.2f}')

# using end=
for i in range(5):
    print(i, end=', ')  # prints same line "0, 1, 2, 3, 4, "

# using sep=
print(1, 2, 3, 4, 5, 6, 7, 8, sep=', ')     # prints "1, 2, 3, 4, 5, 6, 7, 8"

# if elif statements
age = 23
if age >= 18:
    if cit == 'true':
        print('can vote')
    else:
        print('no')
else:
    print('no')


x = 25
# test x between 10 and 50
if x >= 25 and x <= 50:
    print('yes')
else:
    print('no')
# True = 1, False = 0
if 10 <= x <= 50:
    print('yes')
else:
    print('no')

# print numbers 5, 10, 15, 20
for i in range(5, 21, 5):
    print(i, end=', ')
for i in [5, 10, 15, 20]:
    print(i, end=', ')

#lists and tuples
values = [1, 2, 3]
numbers = (1, 2, 3)
values.append(99)
print(values)
print(numbers)





