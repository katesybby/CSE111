# 07 Team Activity: Lists

import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)


def append_random_numbers(numbers_list, quantity=1):

    # ERROR: append_random_numbers() missing 1 required positional argument: 'quantity'
    # numbers_list = []
    # quantity = 1

    for _ in range(quantity):
        random_number = random.uniform(1, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


if __name__ == "__main__":
    main()
